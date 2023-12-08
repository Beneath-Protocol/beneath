import './globals.css'

export const metadata = {
    title: 'Beneath Protocol',
    description: 'Decentralized, Interoperable, Backward compatible, Communication protocol',
}

export default function RootLayout({ children }) {
    return (
        <html lang="en">
            <body>{children}</body>
        </html>
    )
}
