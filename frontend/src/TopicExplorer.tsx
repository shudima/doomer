import { useMemo, useState } from 'react';
import { ArrowRight, BookOpen, Check, CircleCheck, LoaderCircle, LogOut, RefreshCw, Search, X } from 'lucide-react';
import type { TopicSummary } from './api';

type Props = {
  topics: TopicSummary[];
  currentId?: string;
  currentPosition: number;
  finishedCount: number;
  totalCount: number;
  refreshing: boolean;
  openingId: string | null;
  disabled: boolean;
  error: string;
  email?: string;
  onSelect: (topic: TopicSummary) => void;
  onRefresh: () => void;
  onChangeEmail: () => void;
};

function searchable(value: string) {
  return value.normalize('NFD').replace(/\p{Diacritic}/gu, '').toLocaleLowerCase();
}

export function TopicExplorer({ topics, currentId, currentPosition, finishedCount, totalCount, refreshing, openingId, disabled,
  error, email, onSelect, onRefresh, onChangeEmail }: Props) {
  const [query, setQuery] = useState('');
  const visible = useMemo(() => {
    const terms = searchable(query).trim().split(/\s+/).filter(Boolean);
    return topics.filter(topic => terms.every(term => searchable(topic.title).includes(term)))
      .sort((a, b) => a.title.localeCompare(b.title));
  }, [topics, query]);

  return <>
    <header className="explorer-heading">
      <div className="eyebrow">YOUR READING ROOM</div>
      <h2>Explore topics<span className="title-dot">.</span></h2>
      <p>Find an idea. Pick up where you left off.</p>
    </header>
    <div className="explorer-completion" role="status"><CircleCheck size={16} aria-hidden="true" /><span><b>{finishedCount}</b> of <b>{totalCount}</b> topics finished</span></div>
    <div className="topic-search">
      <Search size={18} aria-hidden="true" />
      <input type="search" aria-label="Search topics" placeholder="Search topics…" value={query}
        onChange={event => setQuery(event.target.value)} autoComplete="off" spellCheck={false} />
      {query && <button aria-label="Clear topic search" className="clear-topic-search" onClick={() => setQuery('')}><X size={16} /></button>}
    </div>
    <div className="explorer-caption" aria-live="polite">
      <span>{visible.length} {visible.length === 1 ? 'topic' : 'topics'}{query.trim() ? ' found' : ' in your library'}</span>
      {refreshing ? <span className="explorer-refreshing"><LoaderCircle className="spin" size={12} /> Updating</span> :
        <button className="explorer-refresh" aria-label="Refresh topics" onClick={onRefresh} disabled={disabled}><RefreshCw size={13} /></button>}
    </div>
    {error && <div className="explorer-error" role="alert"><span>{error}</span><button onClick={onRefresh}>Retry</button></div>}
    <div className="explorer-list" role="region" aria-label="Available topics" aria-busy={refreshing}>
      {visible.length > 0 ? <ul>{visible.map(topic => {
        const active = topic.id === currentId;
        const position = Math.min(topic.count - 1, Math.max(0, active ? currentPosition : topic.position));
        if (topic.finished) return <li key={topic.id}>
          <div className="topic-row finished-topic" aria-label={`Finished topic: ${topic.title}`}>
            <span className="topic-row-icon"><CircleCheck size={19} strokeWidth={1.5} /></span>
            <span className="topic-row-content"><span className="topic-row-title">{topic.title}</span>
              <span className="topic-row-meta"><span className="topic-finished-label"><Check size={11} /> Finished</span><span>{topic.count} dooms</span></span>
            </span>
          </div>
        </li>;
        return <li key={topic.id}>
          <button className={`topic-row ${active ? 'current-topic' : ''}`} onClick={() => onSelect(topic)}
            disabled={disabled || openingId !== null} aria-label={`Open topic: ${topic.title}`} aria-current={active ? 'true' : undefined}>
            <span className="topic-row-icon"><BookOpen size={19} strokeWidth={1.5} /></span>
            <span className="topic-row-content"><span className="topic-row-title">{topic.title}</span>
              <span className="topic-row-meta">Doom {position + 1} of {topic.count}{active && <span className="topic-current-label"><Check size={10} /> Reading</span>}</span>
              <span className="topic-row-progress" aria-hidden="true"><span style={{width:`${((position + 1) / topic.count) * 100}%`}} /></span>
            </span>
            {openingId === topic.id ? <LoaderCircle className="spin topic-row-arrow" size={16} /> : <ArrowRight className="topic-row-arrow" size={16} />}
          </button>
        </li>;
      })}</ul> : <div className="explorer-empty">
        {refreshing ? <><LoaderCircle className="spin" size={26} /><h3>Finding your topics…</h3></> :
          query.trim() ? <><Search size={26} /><h3>No matching topics.</h3><p>Try another word or clear your search.</p><button className="text-button" onClick={() => setQuery('')}>Show all topics</button></> :
          <><BookOpen size={26} /><h3>All caught up.</h3><p>Your topics will appear here when they are added.</p></>}
      </div>}
    </div>
    {email && <footer className="explorer-profile"><span>{email}</span><button onClick={onChangeEmail} disabled={openingId !== null}><LogOut size={13} /> Change email</button></footer>}
  </>;
}
