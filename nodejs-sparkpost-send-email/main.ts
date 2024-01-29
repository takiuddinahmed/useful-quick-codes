import 'dotenv/config'
import Sparkpost from 'sparkpost'


const client = new Sparkpost()
console.log(client)

client.transmissions.send({
    options: {
    //   sandbox: true
    },
    content: {
      from: process.env.SPARK_POST_EMAIL_FROM,
      subject: 'Hello, World!',
      html:'<html><body><p>Testing SparkPost - the world\'s most awesomest email service!</p></body></html>'
    },
    recipients: [
      {address: 'taki1502106@gmail.com'}
    ]
  })
  .then(data => {
    console.log('Woohoo! You just sent your first mailing!');
    console.log(data);
  })
  .catch(err => {
    console.log('Whoops! Something went wrong');
    console.log(err);
  });