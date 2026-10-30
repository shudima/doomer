import { beforeEach, describe, expect, it, vi } from 'vitest';
import { readProfile, saveProfile } from './profile';

describe('remembering an email on this device', () => {
  beforeEach(() => {
    const values = new Map<string,string>();
    vi.stubGlobal('localStorage',{
      getItem:(key:string)=>values.get(key)??null,
      setItem:(key:string,value:string)=>values.set(key,value),
      removeItem:(key:string)=>values.delete(key),
    });
  });
  it('restores a saved profile without any email sign-in step', () => {
    const profile={email:'reader@example.com',profile_id:'a'.repeat(64)};
    saveProfile(profile);
    expect(readProfile()).toEqual(profile);
    saveProfile(null);
    expect(readProfile()).toBeNull();
  });
  it('discards malformed stored profiles', () => {
    localStorage.setItem('doomer.profile.v1','{bad-json');
    expect(readProfile()).toBeNull();
    localStorage.setItem('doomer.profile.v1',JSON.stringify({email:'reader@example.com',profile_id:'invalid'}));
    expect(readProfile()).toBeNull();
  });
  it('keeps the app usable when browser storage is unavailable', () => {
    vi.stubGlobal('localStorage',{getItem:()=>{throw Error('blocked')},setItem:()=>{throw Error('blocked')},removeItem:()=>{throw Error('blocked')}});
    expect(readProfile()).toBeNull();
    expect(()=>saveProfile({email:'reader@example.com',profile_id:'a'.repeat(64)})).not.toThrow();
  });
});
