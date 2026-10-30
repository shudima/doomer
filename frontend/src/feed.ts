export function pickTopic<T extends { id: string }>(topics: T[], exclude?: string, random = Math.random): T | undefined {
  const candidates = topics.filter(t => t.id !== exclude);
  return candidates.length ? candidates[Math.min(candidates.length - 1, Math.floor(random() * candidates.length))] : undefined;
}

export function isTopicSwipe(dx: number, dy: number, elapsed: number) {
  const horizontal = Math.abs(dx);
  return horizontal >= 72 && horizontal > Math.abs(dy) * 1.7 && elapsed < 1100;
}
