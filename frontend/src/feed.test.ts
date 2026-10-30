import { describe, expect, it } from 'vitest';
import { isTopicSwipe, pickTopic } from './feed';
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
  it('requires a deliberate right swipe without stealing vertical scroll or left gestures', () => {
    expect(isTopicSwipe(100, 10, 300)).toBe(true);
    expect(isTopicSwipe(80, 100, 300)).toBe(false);
    expect(isTopicSwipe(-100, 10, 300)).toBe(false);
    expect(isTopicSwipe(10, 0, 300)).toBe(false);
    expect(isTopicSwipe(100, 0, 2000)).toBe(false);
  });
});
