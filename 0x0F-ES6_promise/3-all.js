import { uploadPhoto, createUser } from './utils';

export default async function handleProfileSignup() {
  try {
    const body = await uploadPhoto();
    const name = await createUser();
    console.log(`${body.body} ${name.firstName} ${name.lastName}`);
  } catch (error) {
    console.log('Signup system offline');
  }
}
