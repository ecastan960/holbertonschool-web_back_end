import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const body = uploadPhoto();
  const name = createUser();
  let result = '';
  body.then((text) => { result = text.body; });
  body.catch(() => new Error('Signup system offline'));
  name.then((text) => { result += ` ${text.firstName} ${text.lastName}`; console.log(result); });
  name.catch(() => new Error('Signup system offline'));
}
