type AuthFailure = { code?: string; message?: string; name?: string; status?: number };

export function signInErrorMessage(error: unknown): string {
  const failure = error && typeof error === 'object' ? error as AuthFailure : {};
  switch (failure.code) {
    case 'otp_disabled':
    case 'signup_disabled':
    case 'user_not_found':
      return 'This email is not enabled for sign-in yet. Add your account in Supabase Authentication → Users, then try again.';
    case 'email_address_not_authorized':
      return 'Supabase email delivery is not enabled for this address. Use an approved project-team email or configure a custom SMTP sender.';
    case 'over_email_send_rate_limit':
      return 'The email sending limit has been reached. Wait before requesting another link, or check the email provider’s limits.';
    case 'over_request_rate_limit':
      return 'Too many sign-in attempts. Please wait before trying again.';
    case 'email_provider_disabled':
      return 'Email sign-in is disabled. Enable the Email provider in Supabase Authentication.';
    case 'email_address_invalid':
      return 'Please enter a valid email address.';
  }
  if (failure.status === 429) return 'Too many sign-in attempts. Please wait before trying again.';
  if (failure.status === 401 || failure.status === 403) {
    return 'The sign-in service rejected the app configuration. Check the Supabase project URL and publishable key.';
  }
  if (failure.name === 'AuthRetryableFetchError' || failure.message === 'Failed to fetch') {
    return 'Could not reach the sign-in service. Check your connection and try again.';
  }
  if (failure.name === 'AuthApiError' && failure.message) {
    return `Supabase could not send the sign-in email: ${failure.message.slice(0, 250)}`;
  }
  return 'Could not send a sign-in link. Please try again.';
}
