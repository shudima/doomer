export type Profile = { email: string; profile_id: string };
const key = 'doomer.profile.v1';
export function readProfile(): Profile | null {
  try {
    const value = JSON.parse(localStorage.getItem(key) ?? 'null');
    return value && typeof value.email === 'string' && /^[0-9a-f]{64}$/.test(value.profile_id) ? value : null;
  } catch { return null; }
}
export function saveProfile(profile: Profile | null) {
  try {
    if (profile) localStorage.setItem(key, JSON.stringify(profile));
    else localStorage.removeItem(key);
  } catch { /* Reading still works when browser storage is unavailable. */ }
}
