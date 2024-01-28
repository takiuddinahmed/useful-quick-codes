import 'dotenv/config'
import nodemailer from 'nodemailer'


const sender_email = process.env.SENDER_EMAIL_ADDESS;
const app_password = process.env.APP_PASSWORD;


// create reusable transporter object using the default SMTP transport
export const transporter = nodemailer.createTransport({
  service: "gmail",
  host: "smtp.gmail.com",
  port: 587,
  secure: false,
  auth: {
    user: sender_email,
    pass: app_password,
  },
});