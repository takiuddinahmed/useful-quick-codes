import "dotenv/config";

import { transporter } from "./transporter";


export async function sendEmail(to: string | string[], subject: string, html: string) {
    return await transporter.sendMail({
        from: `No Reply Email <${process.env.SENDER_EMAIL_ADDESS}>`,
        to,
        subject,
        html
    })
}