import { useCallback, useEffect, useRef, useState } from 'react';
import type { FormEvent, TouchEvent } from 'react';
import { ArrowDown, ArrowRight, Check, CheckCheck, CircleCheck, ExternalLink, Heart, LoaderCircle, MoreHorizontal, RefreshCw, ThumbsDown, WifiOff, X } from 'lucide-react';
import { api, ApiError, clearImages, imageFor, setProfileId } from './api';
import type { Config, Doom, Library, Reaction, Topic, TopicSummary } from './api';
import { isTopicSwipe, pickTopic, visibleDoomIndex } from './feed';
import { readProfile, saveProfile } from './profile';
import type { Profile } from './profile';
import { TopicExplorer } from './TopicExplorer';
import { DoomMarkdown } from './DoomMarkdown';
import type { Figure } from './DoomMarkdown';

function Orbit({ small = false }: { small?: boolean }) {
  return <span className={`orbit ${small ? 'small' : ''}`} aria-hidden="true"><i /><i /><b /></span>;
}

function EmailSetup({ onContinue }: { onContinue: (profile: Profile) => void }) {
  const [email, setEmail] = useState('');
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState('');
  async function submit(event: FormEvent) {
    event.preventDefault(); setBusy(true); setError('');
    try {
      const profile = await api<Profile>('/api/profile', {method:'POST', body:JSON.stringify({email})});
      onContinue(profile);
    } catch (error) { setError(error instanceof Error ? error.message : 'Could not open your profile. Please try again.'); }
    finally { setBusy(false); }
  }
  return <main className="login-shell">
    <div className="login-top"><Orbit /><span className="wordmark">doomer<span>.</span></span></div>
    <div className="login-orbits" aria-hidden="true"><Orbit /></div>
    <section className="login-content">
      <div className="eyebrow"><span className="live-dot" /> A BETTER KIND OF SCROLL</div>
      <h1>A little less noise.<br /><em>A little more knowing.</em></h1>
      <p>Set your email to keep your place.<br />Use the same email on every device.</p>
      <form onSubmit={submit}>
        <label htmlFor="email">YOUR EMAIL</label>
        <input id="email" type="email" autoComplete="email" inputMode="email" placeholder="you@example.com" value={email} onChange={e => setEmail(e.target.value)} required />
        <button className="primary" disabled={busy}>{busy ? <LoaderCircle className="spin" size={19} /> : <>Start reading <ArrowRight size={18} /></>}</button>
        {error && <p className="form-error" role="alert">{error}</p>}
      </form>
      <p className="private-note">No sign-in links. No email will be sent.</p>
    </section>
  </main>;
}

export function App({ config }: { config: Config }) {
  const [profile, setProfile] = useState<Profile | null>(() => readProfile());
  function useProfile(next: Profile) {
    saveProfile(next); setProfileId(next.profile_id); setProfile(next);
  }
  function resetProfile() {
    clearImages(); saveProfile(null); setProfileId(''); setProfile(null);
  }
  if (config.auth_mode !== 'local' && !profile) return <EmailSetup onContinue={useProfile} />;
  return <Reader key={profile?.profile_id ?? 'local'} config={config} profile={profile} onChangeEmail={resetProfile} />;
}

function doomTop(scroller: HTMLDivElement, index: number) {
  return (scroller.children.item(index) as HTMLElement | null)?.offsetTop ?? 0;
}

type SaveState = 'saved' | 'saving' | 'error';
function Reader({ config, profile, onChangeEmail }: { config: Config; profile: Profile | null; onChangeEmail: () => void }) {
  const [library, setLibrary] = useState<Library | null>(null);
  const [topic, setTopic] = useState<Topic | null>(null);
  const [position, setPosition] = useState(0);
  const [loading, setLoading] = useState(true);
  const [loadError, setLoadError] = useState('');
  const [toast, setToast] = useState('');
  const [saveState, setSaveState] = useState<SaveState>('saved');
  const [menu, setMenu] = useState(false);
  const [explorerBusy, setExplorerBusy] = useState(false);
  const [explorerError, setExplorerError] = useState('');
  const [openingTopicId, setOpeningTopicId] = useState<string | null>(null);
  const [finishDialog, setFinishDialog] = useState(false);
  const [figure, setFigure] = useState<Figure | null>(null);
  const [figureZoom, setFigureZoom] = useState(false);
  const [actionBusy, setActionBusy] = useState(false);
  const [online, setOnline] = useState(navigator.onLine);
  const container = useRef<HTMLDivElement>(null);
  const version = useRef(0);
  const currentTopic = useRef<Topic | null>(null);
  const pending = useRef<{ topicId: string; doomId: string } | null>(null);
  const saving = useRef<Promise<void> | null>(null);
  const alive = useRef(true);
  const transition = useRef(false);
  const swipeStart = useRef<{x:number; y:number; at:number} | null>(null);
  const toastTimer = useRef<ReturnType<typeof setTimeout> | undefined>(undefined);

  const notify = useCallback((message: string) => {
    setToast(message); clearTimeout(toastTimer.current);
    toastTimer.current = setTimeout(() => setToast(''), 4200);
  }, []);

  const flushProgress = useCallback((): Promise<void> => {
    if (saving.current) return saving.current;
    const task = (async () => {
      while (pending.current) {
        const next = pending.current;
        if (alive.current) setSaveState('saving');
        try {
          const result = await api<{version:number}>(`/api/topics/${next.topicId}/progress`, {
            method:'PUT', body:JSON.stringify({ doom_id:next.doomId, expected_version:version.current }),
          });
          version.current = result.version;
          if (pending.current === next) pending.current = null;
        } catch (error) {
          if (alive.current) {
            setSaveState('error');
            notify(error instanceof ApiError && error.status === 409 ? error.message : 'Your place could not be saved. Tap Retry to keep it.');
          }
          throw error;
        }
      }
      if (alive.current) setSaveState('saved');
    })();
    saving.current = task;
    task.finally(() => { saving.current = null; }).catch(() => undefined);
    return task;
  }, [notify]);

  const openTopic = useCallback(async (summary: TopicSummary) => {
    if (transition.current) return;
    transition.current = true;
    try {
      await flushProgress();
      setLoading(true); setLoadError('');
      const data = await api<Topic>(`/api/topics/${summary.id}`);
      currentTopic.current = data; version.current = data.version;
      setTopic(data); setPosition(data.position); setSaveState('saved');
    } catch (error) {
      if (!pending.current) setLoadError(error instanceof Error ? error.message : 'Could not open this topic.');
      throw error;
    } finally { transition.current = false; setLoading(false); }
  }, [flushProgress]);

  const loadFeed = useCallback(async () => {
    setLoading(true); setLoadError('');
    try {
      const data = await api<Library>('/api/topics'); setLibrary(data);
      const selected = pickTopic(data.topics);
      if (selected) await openTopic(selected);
      else { setTopic(null); currentTopic.current = null; }
    } catch (error) { setLoadError(error instanceof Error ? error.message : 'Could not reach your feed.'); }
    finally { setLoading(false); }
  }, [openTopic]);

  useEffect(() => {
    alive.current = true; void loadFeed();
    return () => { alive.current = false; clearTimeout(toastTimer.current); clearImages(); };
  }, [loadFeed]);

  useEffect(() => {
    function connected() { setOnline(true); if (pending.current) void flushProgress().catch(() => undefined); }
    const offline = () => setOnline(false);
    window.addEventListener('online', connected); window.addEventListener('offline', offline);
    const beforeLeave = (e: BeforeUnloadEvent) => { if (pending.current) { e.preventDefault(); e.returnValue = ''; } };
    window.addEventListener('beforeunload', beforeLeave);
    return () => { window.removeEventListener('online', connected); window.removeEventListener('offline', offline); window.removeEventListener('beforeunload', beforeLeave); };
  }, [flushProgress]);

  useEffect(() => {
    let refreshing = false;
    async function refreshOnReturn() {
      if (document.hidden || !navigator.onLine || transition.current || refreshing) return;
      refreshing = true;
      try {
        await flushProgress();
        const latest = await api<Library>('/api/topics');
        setLibrary(latest);
        const current = latest.topics.find(t => t.id === currentTopic.current?.id);
        if (current) await openTopic(current);
        else await loadFeed();
      } catch { /* Existing save errors stay visible; a later foreground or reload can retry reads. */ }
      finally { refreshing = false; }
    }
    window.addEventListener('focus', refreshOnReturn);
    document.addEventListener('visibilitychange', refreshOnReturn);
    return () => { window.removeEventListener('focus', refreshOnReturn); document.removeEventListener('visibilitychange', refreshOnReturn); };
  }, [flushProgress, openTopic, loadFeed]);

  // Restore the saved doom before paint of the first scroll interaction.
  useEffect(() => {
    if (!topic || !container.current || loading) return;
    const scroller = container.current;
    scroller.scrollTop = doomTop(scroller, topic.position);
    const resize = new ResizeObserver(() => {
      const index = Number(scroller.dataset.position ?? topic.position);
      scroller.scrollTop = doomTop(scroller, index);
    });
    resize.observe(scroller);
    return () => resize.disconnect();
  }, [topic?.id, loading]);

  // A settled, snapped card is the current doom, not merely one passing through the viewport.
  useEffect(() => {
    const scroller = container.current;
    if (!scroller || !topic || loading) return;
    let timeout: ReturnType<typeof setTimeout>;
    function settled() {
      const cards = Array.from(scroller!.children, child => {
        const card = child as HTMLElement;
        return {top:card.offsetTop, height:card.offsetHeight};
      });
      const index = visibleDoomIndex(cards, scroller!.scrollTop, scroller!.clientHeight);
      scroller!.dataset.position = String(index);
      setPosition(previous => {
        if (previous !== index && currentTopic.current?.id === topic!.id) {
          pending.current = {topicId:topic!.id, doomId:topic!.dooms[index].id};
          queueMicrotask(() => void flushProgress().catch(() => undefined));
        }
        return index;
      });
    }
    const scroll = () => { clearTimeout(timeout); timeout = setTimeout(settled, 140); };
    scroller.addEventListener('scroll', scroll, {passive:true});
    return () => { clearTimeout(timeout); scroller.removeEventListener('scroll', scroll); };
  }, [topic?.id, loading, flushProgress]);

  async function retryProgress() {
    try { await flushProgress(); notify('Your place is saved.'); }
    catch (error) {
      if (error instanceof ApiError && error.status === 409 && topic) {
        pending.current = null;
        const summary = topic;
        await openTopic(summary).catch(() => undefined);
        notify('Restored the latest position from your other device.');
      }
    }
  }

  async function anotherTopic() {
    if (loading || actionBusy || finishDialog || figure || menu || transition.current) return;
    try {
      await flushProgress();
      const latest = await api<Library>('/api/topics'); setLibrary(latest);
      const next = pickTopic(latest.topics, topic?.id);
      if (next) await openTopic(next);
      else notify('You’re in your only unfinished topic. More ideas will land here as you add them.');
    } catch (error) { if (!pending.current) notify(error instanceof Error ? error.message : 'Could not switch topics.'); }
  }

  async function refreshExplorer() {
    setExplorerBusy(true); setExplorerError('');
    try {
      await flushProgress();
      const latest = await api<Library>('/api/topics');
      setLibrary(latest);
    } catch (error) {
      setExplorerError(error instanceof Error ? error.message : 'Could not refresh topics.');
    } finally { setExplorerBusy(false); }
  }

  function showExplorer() {
    setMenu(true);
    void refreshExplorer();
  }

  async function selectTopic(summary: TopicSummary) {
    if (openingTopicId || loading || transition.current) return;
    setOpeningTopicId(summary.id); setExplorerError('');
    try {
      await openTopic(summary);
      setMenu(false);
    } catch (error) {
      setLoadError('');
      setExplorerError(error instanceof Error ? error.message : 'Could not open this topic.');
      if (error instanceof ApiError && error.status === 410) void refreshExplorer();
    } finally { setOpeningTopicId(null); }
  }

  async function reaction(value: Exclude<Reaction, null>) {
    if (!topic || actionBusy) return;
    const doom = topic.dooms[position];
    const target = doom.reaction === value ? null : value;
    setActionBusy(true);
    try {
      const result = await api<{reaction:Reaction}>(`/api/dooms/${doom.id}/reaction`, { method:'PUT', body:JSON.stringify({value:target}) });
      setTopic(previous => previous ? {...previous, dooms:previous.dooms.map(d => d.id === doom.id ? {...d,reaction:result.reaction} : d)} : previous);
      notify(result.reaction === 'like' ? 'Liked. An idea worth keeping.' : result.reaction === 'dislike' ? 'Feedback saved.' : 'Reaction removed.');
    } catch { notify('Reaction wasn’t saved. Please try again.'); }
    finally { setActionBusy(false); }
  }

  async function finishTopic() {
    if (!topic || actionBusy) return;
    setActionBusy(true);
    try {
      await flushProgress();
      await api(`/api/topics/${topic.id}/finish`, { method:'POST' });
      setFinishDialog(false); currentTopic.current = null; setTopic(null);
      await loadFeed(); notify('Topic finished. It won’t appear in your feed again.');
    } catch { notify('Topic wasn’t marked finished. Please try again.'); }
    finally { setActionBusy(false); }
  }

  function nextDoom() {
    if (!container.current || !topic) return;
    if (position === topic.dooms.length-1) { setFinishDialog(true); return; }
    container.current.scrollTo({ top:doomTop(container.current, position + 1), behavior:window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth' });
  }
  function touchStart(event: TouchEvent) {
    const target = event.target as HTMLElement;
    if (target.closest('button, a, input, pre, .markdown-table')) { swipeStart.current = null; return; }
    const touch = event.changedTouches[0];
    swipeStart.current = {x:touch.clientX, y:touch.clientY, at:performance.now()};
  }
  function touchEnd(event: TouchEvent) {
    if (!swipeStart.current) return;
    const touch = event.changedTouches[0], start = swipeStart.current;
    if (isTopicSwipe(touch.clientX-start.x, touch.clientY-start.y, performance.now()-start.at)) void anotherTopic();
    swipeStart.current = null;
  }
  function keyboard(event: React.KeyboardEvent) {
    if (menu || finishDialog || figure || (event.target as HTMLElement).closest('button, input, a, pre, .markdown-table')) return;
    if (event.key === 'ArrowRight' || event.key === 'ArrowLeft') { event.preventDefault(); void anotherTopic(); }
    if (event.key === 'ArrowDown' || event.key === ' ') { event.preventDefault(); nextDoom(); }
    if (event.key === 'ArrowUp' && container.current) { event.preventDefault(); container.current.scrollTo({top:doomTop(container.current, Math.max(0, position - 1)), behavior:'smooth'}); }
  }

  const current = topic?.dooms[position];
  return <main className="app-shell" onKeyDown={keyboard} tabIndex={-1}>
    <header className="header">
      <a className="brand" href="/" aria-label="Doomer home"><Orbit small /><span className="wordmark">doomer<span>.</span></span></a>
      <div className="header-right">
        <button className={`sync ${saveState}`} onClick={saveState === 'error' ? retryProgress : undefined} aria-label={saveState === 'error' ? 'Retry saving progress' : 'Progress sync status'}>
          {!online ? <WifiOff size={12} /> : saveState === 'saving' ? <LoaderCircle className="spin" size={12} /> : saveState === 'error' ? <RefreshCw size={12} /> : <span className="live-dot" />}
          <span>{saveState === 'error' ? 'Retry save' : !online ? 'Offline' : saveState === 'saving' ? 'Saving' : config.auth_mode === 'local' ? 'Saved locally' : 'Synced'}</span>
        </button>
        <button className="icon-button menu-button" aria-label="Explore topics" onClick={showExplorer}><MoreHorizontal size={23} /></button>
      </div>
    </header>
    <section className="topic-context" aria-label="Current topic">
      {topic && current ? <>
        <div className="topic-context-copy">
          <div className="topic-context-title">{topic.title}</div>
          <SourceReference doom={current} />
        </div>
        <div className="doom-number" aria-label={`Doom ${position + 1} of ${topic.count}`}><b>{position + 1}</b><span>/</span>{topic.count}</div>
      </> : <span className="topic-context-title">Your topic library</span>}
    </section>
    {loadError ? <section className="centered feed-state"><WifiOff size={30} /><h1>A small interruption.</h1><p>{loadError}</p><button className="primary" onClick={() => void loadFeed()}>Try again <RefreshCw size={16} /></button><button className="text-button" onClick={onChangeEmail}>Change email</button></section> :
     loading ? <section className="centered feed-state"><Orbit /><p className="muted">Finding your next good idea…</p></section> :
     !topic ? <section className="centered feed-state empty"><div className="empty-mark"><CheckCheck size={35} /></div><div className="eyebrow">A LITTLE ROOM TO THINK</div><h1>{library?.total_topics ? 'All caught up.' : 'Good ideas are on their way.'}</h1><p>{library?.total_topics ? 'You’ve finished every topic in your feed. Come back when there’s something new to get lost in.' : 'Your feed will be here when your first topic is added.'}</p><button className="text-button" onClick={() => void loadFeed()}>Check for new topics <RefreshCw size={14} /></button></section> :
     <section className="reader" aria-label="Doom feed">
       <div ref={container} className="doom-scroll" data-position={position} onTouchStart={touchStart} onTouchEnd={touchEnd} onTouchCancel={() => { swipeStart.current = null; }} aria-label="Scroll for dooms; swipe left or right for another topic" tabIndex={0}>
         {topic.dooms.map((doom, index) => <DoomCard key={doom.id} doom={doom} topic={topic} active={Math.abs(index-position) <= 1} onFigure={next => { setFigure(next); setFigureZoom(false); }} />)}
       </div>
       <aside className="action-rail" aria-label="Doom actions">
         <button className={`rail-button ${current?.reaction === 'like' ? 'selected liked' : ''}`} onClick={() => void reaction('like')} disabled={actionBusy} aria-label="Like this doom" aria-pressed={current?.reaction === 'like'}><span><Heart size={24} fill={current?.reaction === 'like' ? 'currentColor' : 'none'} strokeWidth={1.6} /></span><small>Like</small></button>
         <button className={`rail-button ${current?.reaction === 'dislike' ? 'selected' : ''}`} onClick={() => void reaction('dislike')} disabled={actionBusy} aria-label="Dislike this doom" aria-pressed={current?.reaction === 'dislike'}><span><ThumbsDown size={23} strokeWidth={1.6} /></span><small>Dislike</small></button>
         <div className="rail-divider" />
         <button className="rail-button finish" onClick={() => setFinishDialog(true)} disabled={actionBusy} aria-label="Finish this topic"><span><CircleCheck size={24} strokeWidth={1.6} /></span><small>Finish</small></button>
       </aside>
       <button className="next-doom" aria-label={position === topic.count-1 ? 'Finish topic' : 'Next doom'} onClick={nextDoom} disabled={actionBusy}><ArrowDown size={18} /></button>
       <div className="read-progress" aria-hidden="true"><span style={{width:`${((position+1)/topic.count)*100}%`}} /></div>
     </section>}
    {toast && <div className="toast" role="status"><Check size={15} /><span>{toast}</span></div>}
    {finishDialog && topic && <Modal title="Ready to close this chapter?" onClose={() => !actionBusy && setFinishDialog(false)}>
      <div className="sheet-symbol"><CircleCheck size={28} /></div><div className="eyebrow">FINISH TOPIC</div><h2>Ready to close<br /><em>this chapter?</em></h2>
      <p>“{topic.title}” will leave your feed for good. Your reactions will stay saved.</p>
      <button className="primary" onClick={() => void finishTopic()} disabled={actionBusy}>{actionBusy ? <LoaderCircle className="spin" size={18} /> : <>Finish topic <CheckCheck size={19} /></>}</button>
      <button className="text-button" onClick={() => setFinishDialog(false)} disabled={actionBusy}>Keep reading</button>
    </Modal>}
    {figure && <Modal title="Source figure" className="figure-sheet" onClose={() => setFigure(null)}>
      <div className="figure-viewer-controls"><button className="text-button" onClick={() => setFigureZoom(!figureZoom)}>{figureZoom ? 'Fit image' : 'Zoom in'}</button></div>
      <div className={`figure-viewer ${figureZoom ? 'zoomed' : ''}`} tabIndex={0} aria-label="Scrollable source figure"><img src={figure.url} alt={figure.alt} /></div>
      <p className="figure-viewer-caption">{figure.alt}</p>
    </Modal>}
    {menu && <Modal title="Explore topics" className="explorer-sheet" onClose={() => !openingTopicId && setMenu(false)}>
      <TopicExplorer topics={[...(library?.topics ?? []), ...(library?.finished_topics ?? [])]} currentId={topic?.id} currentPosition={position}
        finishedCount={library?.finished_count ?? 0} totalCount={library?.total_topics ?? 0}
        refreshing={explorerBusy} openingId={openingTopicId} disabled={loading || explorerBusy}
        error={explorerError} email={profile?.email} onSelect={summary => void selectTopic(summary)}
        onRefresh={() => void refreshExplorer()} onChangeEmail={async () => {
          try { await flushProgress(); onChangeEmail(); }
          catch { setExplorerError('Save your place before changing email.'); }
        }} />
    </Modal>}
  </main>;
}

function SourceReference({ doom }: { doom: Doom }) {
  const url = doom.source_url ? new URL(doom.source_url) : null;
  return <div className="topic-context-source">
    <span>Source: {url ? <a href={url.href} target="_blank" rel="noopener noreferrer">{url.hostname.replace(/^www\./, '')}<ExternalLink size={10} aria-hidden="true" /></a> : doom.source_type === 'pdf' ? 'PDF' : 'Original source'}</span>
    <span aria-hidden="true">·</span><span className="topic-context-locator">{doom.source_locator}</span>
  </div>;
}

function DoomCard({ doom, topic, active, onFigure }: { doom:Doom; topic:Topic; active:boolean; onFigure:(figure:Figure)=>void }) {
  const [background, setBackground] = useState('');
  useEffect(() => {
    let mounted = true;
    if (active) imageFor(doom.image_url).then(url => { if (mounted) setBackground(url); }).catch(() => undefined);
    return () => { mounted = false; };
  }, [doom.image_url, active]);
  return <article className="doom-card" lang={doom.language} dir={/^(he|ar|fa|ur)(-|$)/.test(doom.language) ? 'rtl' : 'ltr'} aria-label={`Doom ${doom.sort_order} of ${topic.count}: ${doom.title}`}>
    {background && <img className="card-art" src={background} alt="" draggable={false} />}
    <div className="card-shade" />
    <div className="reading-content">
      <h1 className={doom.title.length > 42 ? 'long-title' : ''}>{doom.title}<span className="title-dot">.</span></h1>
      <div className="prose">{doom.format === 'markdown' ? <DoomMarkdown text={doom.text} assets={doom.assets ?? {}} active={active} onFigure={onFigure} /> : doom.text.split(/\n\s*\n/).map((paragraph,index) => <p key={index}>{paragraph}</p>)}</div>
      {doom.sort_order === topic.count && <p className="end-note"><CheckCheck size={13} /> Last doom in this topic. Finish whenever you’re ready.</p>}
    </div>
  </article>;
}

function Modal({title, onClose, children, className = ''}: {title:string; onClose:()=>void; children:React.ReactNode; className?:string}) {
  const box = useRef<HTMLDivElement>(null);
  const close = useRef(onClose); close.current = onClose;
  useEffect(() => {
    const previous = document.activeElement as HTMLElement | null;
    box.current?.focus();
    const handler = (event: KeyboardEvent) => {
      if (event.key === 'Escape') close.current();
      if (event.key === 'Tab' && box.current) {
        const nodes = Array.from(box.current.querySelectorAll<HTMLElement>('button:not(:disabled), a, input'));
        if (!nodes.length) return;
        if (event.shiftKey && (document.activeElement === nodes[0] || document.activeElement === box.current)) { event.preventDefault(); nodes.at(-1)?.focus(); }
        else if (!event.shiftKey && (document.activeElement === nodes.at(-1) || document.activeElement === box.current)) { event.preventDefault(); nodes[0].focus(); }
      }
    };
    document.addEventListener('keydown', handler);
    return () => { document.removeEventListener('keydown', handler); previous?.focus(); };
  }, []);
  return <div className="modal-backdrop" onClick={onClose}><section ref={box} role="dialog" aria-modal="true" aria-label={title} className={`sheet ${className}`} tabIndex={-1} onClick={e => e.stopPropagation()}><div className="sheet-handle" /><button className="icon-button sheet-close" aria-label="Close dialog" onClick={onClose}><X size={19} /></button>{children}</section></div>;
}
