import { createQueue } from 'kue';

const queue = createQueue();

const blackNumbers = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
  if (blackNumbers.includes(phoneNumber)) done(new Error(`Phone number ${phoneNumber} is blacklisted`));

  job.progress(0, 50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
};

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
