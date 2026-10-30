export type Config = {
  auth_mode: 'local' | 'email'; sentry_dsn: string; release: string;
};
export type Reaction = 'like' | 'dislike' | null;
export type Doom = {
  id: string; title: string; text: string; sort_order: number;
  language: string; source_locator: string; image_url: string; reaction: Reaction;
};
export type TopicSummary = { id: string; title: string; count: number; doom_id: string; position: number; version: number };
export type Topic = TopicSummary & { dooms: Doom[] };
export type Library = { topics: TopicSummary[]; total_topics: number; finished_count: number; user_id: string };

export class ApiError extends Error {
  constructor(public status: number, message: string) { super(message); }
}
let profileId = '';
export function setProfileId(value: string) { profileId = value; }
export async function api<T>(url: string, init: RequestInit = {}): Promise<T> {
  const response = await fetch(url, {
    ...init, headers: { ...(init.body ? { 'Content-Type': 'application/json' } : {}),
      ...(profileId ? { 'X-Doomer-Profile': profileId } : {}), ...init.headers },
    cache: 'no-store',
  });
  if (!response.ok) {
    const data = await response.json().catch(() => ({}));
    throw new ApiError(response.status, typeof data.detail === 'string' ? data.detail : 'Could not save. Please try again.');
  }
  return response.json();
}

const images = new Map<string, Promise<string>>();
export function imageFor(url: string): Promise<string> {
  if (!images.has(url)) {
    const promise = (async () => {
      const response = await fetch(url, { headers: profileId ? { 'X-Doomer-Profile': profileId } : {}, cache: 'no-store' });
      if (!response.ok) throw new Error('Image unavailable');
      return URL.createObjectURL(await response.blob());
    })();
    images.set(url, promise);
    promise.catch(() => images.delete(url));
  }
  return images.get(url)!;
}
export function clearImages() {
  for (const promise of images.values()) promise.then(URL.revokeObjectURL).catch(() => undefined);
  images.clear();
}
