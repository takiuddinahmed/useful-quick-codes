import {sendEmail} from './send-email'


async function main() {
    const to = 'taki1502106@gmail.com';
    const subject = 'Hello from Taki';
    const html = '<p>Hello this is a file and I updated it....</p>';

    const res = await sendEmail(to, subject, html);
    console.log(res)
}

main()