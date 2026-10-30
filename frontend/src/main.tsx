import React from 'react';
import ReactDOM from 'react-dom/client';
import '@fontsource/dm-sans/latin-400.css';
import '@fontsource/dm-sans/latin-500.css';
import '@fontsource/dm-sans/latin-600.css';
import '@fontsource/newsreader/latin-400.css';
import { App } from './App';
import { api, setProfileId } from './api';
import { readProfile } from './profile';
import type { Config } from './api';
import './style.css';

let reportError: (error: Error) => void = () => undefined;
class Boundary extends React.Component<{children:React.ReactNode}, {failed:boolean}> {
  state = {failed:false};
  static getDerivedStateFromError() { return {failed:true}; }
  componentDidCatch(error:Error) { reportError(error); }
  render() {
    return this.state.failed ? <main className="centered"><h1>A small interruption.</h1><p>Reload Doomer to get back to your feed.</p><button onClick={() => location.reload()}>Reload</button></main> : this.props.children;
  }
}

async function boot() {
  const config = await api<Config>('/api/config');
  setProfileId(readProfile()?.profile_id ?? '');
  if (config.sentry_dsn) {
    const Sentry = await import('@sentry/react');
    Sentry.init({ dsn: config.sentry_dsn, release: config.release,
      sendDefaultPii: false, beforeSend(event) { delete event.user; return event; } });
    reportError = error => Sentry.captureException(error);
  }
  ReactDOM.createRoot(document.getElementById('root')!).render(
    <Boundary>
      <App config={config} />
    </Boundary>
  );
}
boot().catch(() => {
  const root = document.getElementById('root')!;
  root.textContent = '';
  const main = document.createElement('main'); main.className = 'centered';
  const title = document.createElement('h1'); title.textContent = 'Doomer is out of reach.';
  const text = document.createElement('p'); text.textContent = 'Check your connection, then reload to try again.';
  const button = document.createElement('button'); button.textContent = 'Try again'; button.onclick = () => location.reload();
  main.append(title, text, button); root.append(main);
});
