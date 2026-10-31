import React from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import { describe, expect, it } from 'vitest';
import { DoomMarkdown } from './DoomMarkdown';

function render(text: string, assets = {}) {
  return renderToStaticMarkup(<DoomMarkdown text={text} assets={assets} active={false} onFigure={() => undefined} />);
}

describe('Markdown reading', () => {
  it('renders emphasis, lists, tables and literal code as readable content', () => {
    const output = render('One **concept**.\n\n- First\n- Second\n\n| Check | Result |\n| --- | --- |\n| Date | Pass |\n\n```python\nprint("<think>")\n```');
    expect(output).toContain('<strong>concept</strong>');
    expect(output).toContain('<li>First</li>');
    expect(output).toContain('<table>');
    expect(output).toContain('&lt;think&gt;');
  });
  it('omits raw executable markup and unsafe link schemes', () => {
    const output = render('<script>alert(1)</script>\n\n[bad](javascript:alert)\n\n[good](https://example.org/source)');
    expect(output).not.toContain('<script');
    expect(output).not.toContain('href="javascript:');
    expect(output).toContain('rel="noopener noreferrer"');
  });
  it('reserves figure space from API dimensions without using remote or local disk URLs', () => {
    const output = render('![Cache flow](images/cache.webp)', {'images/cache.webp':{url:'/api/topics/cache/assets/token',width:1200,height:600}});
    expect(output).toContain('aspect-ratio:1200 / 600');
    expect(output).toContain('Enlarge image: Cache flow');
    expect(output).not.toContain('src="images/');
    expect(render('![Remote](https://example.org/pixel)')).toContain('Figure unavailable');
  });
  it('keeps Mermaid lazy and preserves surrounding prose', () => {
    const output = render('Before.\n\n```mermaid\nflowchart TD\n A --> B\n```\n\nAfter.');
    expect(output).toContain('Explanation diagram');
    expect(output).toContain('Before.');
    expect(output).toContain('After.');
    expect(output).not.toContain('language-mermaid');
  });
});
