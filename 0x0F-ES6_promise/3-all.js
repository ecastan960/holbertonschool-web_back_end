import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const body = uploadPhoto();
  const name = createUser();
  let result = '';
  body.then((text) => { result = text.body; });
  name.then((text) => { result += ` ${text.firstName} ${text.lastName}`; console.log(result); });
}
