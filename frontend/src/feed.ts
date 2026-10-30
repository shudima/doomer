export function pickTopic<T extends { id: string }>(topics: T[], exclude?: string, random = Math.random): T | undefined {
  const candidates = topics.filter(t => t.id !== exclude);
  return candidates.length ? candidates[Math.min(candidates.length - 1, Math.floor(random() * candidates.length))] : undefined;
}

export function isTopicSwipe(dx: number, dy: number, elapsed: number) {
  const horizontal = Math.abs(dx);
  return horizontal >= 72 && horizontal > Math.abs(dy) * 1.7 && elapsed < 1100;
}


export type DoomLayout = { top: number; height: number };

// A long doom may span more than one screen. Track the card with the most visible
// content instead of dividing the scroll offset by the viewport height.
export function visibleDoomIndex(cards: DoomLayout[], scrollTop: number, viewportHeight: number): number {
  const start = Math.max(0, scrollTop);
  const end = start + viewportHeight;
  let selected = 0;
  let largest = -1;
  cards.forEach((card, index) => {
    const visible = Math.max(0, Math.min(end, card.top + card.height) - Math.max(start, card.top));
    if (visible > largest) { largest = visible; selected = index; }
  });
  return selected;
}
