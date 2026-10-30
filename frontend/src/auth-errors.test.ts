import { describe, expect, it } from 'vitest';
import { signInErrorMessage } from './auth-errors';

describe('sign-in failure guidance', () => {
  it('explains that private sign-in requires an existing app account', () => {
    expect(signInErrorMessage({code:'otp_disabled'})).toContain('Authentication → Users');
    expect(signInErrorMessage({code:'user_not_found'})).toContain('Add your account');
  });
  it('distinguishes sender restrictions from an invalid email address', () => {
    expect(signInErrorMessage({code:'email_address_not_authorized'})).toContain('SMTP');
    expect(signInErrorMessage({code:'email_address_invalid'})).toContain('valid email address');
  });
  it('tells a rate-limited user to wait rather than repeatedly request email', () => {
    expect(signInErrorMessage({code:'over_email_send_rate_limit'})).toContain('Wait');
    expect(signInErrorMessage({status:429})).toContain('wait');
  });
  it('separates network failures and app configuration failures', () => {
    expect(signInErrorMessage({name:'AuthRetryableFetchError'})).toContain('connection');
    expect(signInErrorMessage({status:401})).toContain('publishable key');
  });
  it('retains provider diagnostics without guessing for an unknown failure', () => {
    expect(signInErrorMessage({name:'AuthApiError',message:'Error sending magic link email'})).toContain('Error sending magic link email');
    expect(signInErrorMessage(undefined)).toBe('Could not send a sign-in link. Please try again.');
  });
});
