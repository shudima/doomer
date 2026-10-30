import { describe, expect, it } from 'vitest';
import { isTopicSwipe, pickTopic, visibleDoomIndex } from './feed';
describe('topic navigation', () => {
  it('never returns the current topic or invents a second topic', () => {
    expect(pickTopic([{ id: 'only' }], 'only')).toBeUndefined();
    expect(pickTopic([{ id: 'a' }, { id: 'b' }], 'a', () => 0)?.id).toBe('b');
  });
  it('can select every eligible topic', () => {
    const topics = [{id:'a'}, {id:'b'}, {id:'c'}];
    expect([0, .4, .9].map(r => pickTopic(topics, undefined, () => r)?.id)).toEqual(['a', 'b', 'c']);
    expect(pickTopic([])).toBeUndefined();
  });
  it('requires a deliberate horizontal swipe in either direction without stealing vertical scroll', () => {
    expect(isTopicSwipe(100, 10, 300)).toBe(true);
    expect(isTopicSwipe(80, 100, 300)).toBe(false);
    expect(isTopicSwipe(-100, 10, 300)).toBe(true);
    expect(isTopicSwipe(-80, 100, 300)).toBe(false);
    expect(isTopicSwipe(-10, 0, 300)).toBe(false);
    expect(isTopicSwipe(-100, 0, 2000)).toBe(false);
    expect(isTopicSwipe(10, 0, 300)).toBe(false);
    expect(isTopicSwipe(100, 0, 2000)).toBe(false);
  });
});


describe('progress with long, scrollable dooms', () => {
  const cards = [{top:0,height:1100},{top:1100,height:600},{top:1700,height:850}];
  it('keeps the same doom while scrolling through text taller than the screen', () => {
    expect(visibleDoomIndex(cards, 0, 600)).toBe(0);
    expect(visibleDoomIndex(cards, 500, 600)).toBe(0);
    expect(visibleDoomIndex(cards, 700, 600)).toBe(0);
  });
  it('advances by actual card bounds rather than viewport-sized pages', () => {
    expect(visibleDoomIndex(cards, 900, 600)).toBe(1);
    expect(visibleDoomIndex(cards, 1100, 600)).toBe(1);
    expect(visibleDoomIndex(cards, 1700, 600)).toBe(2);
    expect(visibleDoomIndex(cards, 1950, 600)).toBe(2);
  });
  it('handles viewport changes and iOS top overscroll without inventing progress', () => {
    expect(visibleDoomIndex(cards, -40, 400)).toBe(0);
    expect(visibleDoomIndex(cards, 500, 400)).toBe(0);
    expect(visibleDoomIndex([], 0, 600)).toBe(0);
  });
});
