import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const sizes = [19, 20, 34];
  const result = [];
  for (const size of sizes) {
    result.push(new ClassRoom(size));
  }
  console.log(result);
  return result;
}
