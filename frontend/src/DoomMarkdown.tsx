import { useEffect, useState } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { Expand, RefreshCw } from 'lucide-react';
import { imageFor } from './api';
import type { ContentAsset } from './api';

export type Figure = { url: string; alt: string };
type Props = { text: string; assets: Record<string, ContentAsset>; active: boolean; onFigure: (figure: Figure) => void };

function FigureImage({ asset, alt, active, onFigure }: { asset: ContentAsset; alt: string; active: boolean; onFigure: Props['onFigure'] }) {
  const [source, setSource] = useState('');
  const [error, setError] = useState(false);
  const [attempt, setAttempt] = useState(0);
  useEffect(() => {
    let alive = true;
    if (active) {
      setError(false);
      imageFor(asset.url).then(url => { if (alive) setSource(url); }).catch(() => { if (alive) setError(true); });
    }
    return () => { alive = false; };
  }, [asset.url, active, attempt]);
  const ratio = asset.width && asset.height ? `${asset.width} / ${asset.height}` : '4 / 3';
  return <span className="markdown-figure">
    <button className="figure-image" style={{aspectRatio:ratio}} aria-label={error ? `Retry image: ${alt}` : `Enlarge image: ${alt}`}
      disabled={!source && !error} onClick={() => error ? setAttempt(attempt + 1) : onFigure({url:source,alt})}>
      {source ? <img src={source} alt={alt} width={asset.width ?? undefined} height={asset.height ?? undefined} /> :
        <span className="figure-loading">{error ? <><RefreshCw size={16} /> Retry image</> : 'Loading image…'}</span>}
      {source && <span className="figure-expand"><Expand size={14} /></span>}
    </button>
    <span className="figure-caption">{alt}</span>
  </span>;
}

let diagramNumber = 0;
let diagramQueue = Promise.resolve();
let mermaidModule: Promise<typeof import('mermaid')['default']> | undefined;
function mermaid() {
  mermaidModule ??= import('mermaid').then(({default:renderer}) => {
    renderer.initialize({startOnLoad:false, securityLevel:'strict', theme:'neutral', fontFamily:'DM Sans, sans-serif', flowchart:{htmlLabels:false}});
    return renderer;
  });
  return mermaidModule;
}

function Diagram({ code, active, onFigure }: { code: string; active: boolean; onFigure: Props['onFigure'] }) {
  const [svg, setSvg] = useState('');
  const [error, setError] = useState(false);
  useEffect(() => {
    let alive = true;
    if (active && !svg) {
      const task = diagramQueue.then(async () => {
        if (!alive) return;
        const renderer = await mermaid();
        const result = await renderer.render(`doom-diagram-${++diagramNumber}`, code);
        if (alive) {
          const created = URL.createObjectURL(new Blob([result.svg],{type:'image/svg+xml'}));
          setSvg(created);
        }
      });
      diagramQueue = task.catch(() => { if (alive) setError(true); });
    }
    return () => { alive = false; };
  }, [code, active]);
  useEffect(() => () => { if (svg) URL.revokeObjectURL(svg); }, [svg]);
  return <span className="markdown-figure diagram" aria-label="Explanation diagram">
    {svg ? <button className="figure-image" aria-label="Enlarge diagram" onClick={() => onFigure({url:svg,alt:'Explanation diagram'})}><img src={svg} alt="Explanation diagram" /><span className="figure-expand"><Expand size={14} /></span></button> :
      error ? <pre className="diagram-source"><code>{code}</code></pre> : <span className="figure-loading">{active ? 'Drawing diagram…' : 'Diagram'}</span>}
    {error && <span className="figure-caption">Diagram source shown because the drawing could not load.</span>}
  </span>;
}

function AssetLink({ asset, name, children, active }: { asset: ContentAsset; name: string; children: React.ReactNode; active: boolean }) {
  const [source, setSource] = useState('');
  useEffect(() => {
    let alive = true;
    if (active) imageFor(asset.url).then(url => { if (alive) setSource(url); }).catch(() => undefined);
    return () => { alive = false; };
  }, [asset.url, active]);
  return source ? <a href={source} download={name.split('/').pop()}>{children}</a> : <span>{children}</span>;
}

export function DoomMarkdown({ text, assets, active, onFigure }: Props) {
  return <div className="markdown-content"><ReactMarkdown remarkPlugins={[remarkGfm]} skipHtml components={{
    img:({src,alt}) => assets[src ?? ''] ? <FigureImage asset={assets[src!]} alt={alt || 'Source figure'} active={active} onFigure={onFigure} /> : <span className="figure-caption">Figure unavailable: {alt}</span>,
    a:({href,children}) => assets[href ?? ''] ? <AssetLink asset={assets[href!]} name={href!} active={active}>{children}</AssetLink> :
      href && /^https?:\/\//.test(href) ? <a href={href} target="_blank" rel="noopener noreferrer">{children}</a> : <span>{children}</span>,
    pre:({children,node}) => node?.children.some(child => child.type === 'element' && child.properties.className instanceof Array && child.properties.className.includes('language-mermaid')) ? <>{children}</> : <pre>{children}</pre>,
    code:({className,children}) => className === 'language-mermaid' ? <Diagram code={String(children).trim()} active={active} onFigure={onFigure} /> : <code className={className}>{children}</code>,
    table:({children}) => <div className="markdown-table" tabIndex={0} aria-label="Scrollable comparison table"><table>{children}</table></div>,
  }}>{text}</ReactMarkdown></div>;
}
