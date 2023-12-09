import './globals.css'
import { Providers } from "@/components/provider/provider";

export const metadata = {
    title: 'Beneath Protocol',
    description: 'Decentralized, Interoperable, Backward compatible, Communication protocol',
}

export default function RootLayout({ children }) {
    return (
        <html lang="en">
            <body>
                <Providers>
                    {children}
                </Providers>
            </body>
        </html>
    )
}
