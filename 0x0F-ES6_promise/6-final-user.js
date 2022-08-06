import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const name = await signUpUser(firstName, lastName);
  let file;
  try {
    file = await uploadPhoto(fileName);
  } catch (err) {
    file = err.toString();
  }
  return [
    { value: name, status: 'fulfilled' },
    { value: file, status: 'rejected' }
  ];
}
