import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "AXIOM — California Property Intelligence",
  description: "A source-grounded command surface for California property research.",
  openGraph: {
    title: "AXIOM — Order the Signal",
    description: "Source-grounded California property intelligence.",
    images: ["/axiom-social-card.png"],
  },
  twitter: {
    card: "summary_large_image",
    title: "AXIOM — Order the Signal",
    description: "Source-grounded California property intelligence.",
    images: ["/axiom-social-card.png"],
  },
  icons: {
    icon: "/favicon.svg",
    shortcut: "/favicon.svg",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="dark">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
