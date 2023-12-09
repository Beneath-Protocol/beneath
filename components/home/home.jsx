"use client"
import React from 'react'
import SearchBar from '../ui/searchbar'
import logo from '../../public/assets/logo.svg'
import Image from 'next/image'
import {
  Menubar,
  MenubarContent,
  MenubarItem,
  MenubarMenu,
  MenubarSeparator,
  MenubarShortcut,
  MenubarTrigger,
} from "@/components/ui/menubar"
import { Sidebar } from '../ui/sidebar'
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { useMessage } from '@/context/contextProvider'
import { useEffect } from 'react'
import Directchat from '../directchat/directchat'
import Groupchat from '../groupchat/groupchat'


function MailPage() {

  const { sidebarstep} = useMessage();
  // useEffect(() => {
  //   console.log(sidebarstep)
  // }, [sidebarstep])

  return (
    <div className='flex flex-col'>

      {/* TopBar */}
      <div className='flex w-full justify-between py-6 px-10'>
        <Image src={logo} alt='logo' />
        <div className='w-fit'>
          <SearchBar />
        </div>
        <div className='w-12 h-12 rounded-full bg-blue-200'></div>
      </div>

      <div className='flex gap-12 mr-4'>
        {/* <Menubar>
          <MenubarMenu>
            <MenubarTrigger>Inbox</MenubarTrigger>
            <MenubarContent>
              <MenubarItem>New Window</MenubarItem>
              <MenubarSeparator />
              <MenubarItem>Share</MenubarItem>
              <MenubarSeparator />
              <MenubarItem>Print</MenubarItem>
            </MenubarContent>
          </MenubarMenu>

          <MenubarMenu>
            <MenubarTrigger>File</MenubarTrigger>
            <MenubarContent>
              <MenubarItem>New Window</MenubarItem>
              <MenubarSeparator />
              <MenubarItem>Share</MenubarItem>
              <MenubarSeparator />
              <MenubarItem>Print</MenubarItem>
            </MenubarContent>
          </MenubarMenu>
        </Menubar> */}


        <Sidebar options={['Inbox', 'Direct Messages', 'Group Chats', 'Your Spaces']} />
        {sidebarstep === 0 &&
          <div className='flex flex-col gap-5 p-2 shadow-lg shadow-slate-800 w-full rounded-md'>
            <Tabs defaultValue="allmails" className="w-full">
              <TabsList className="w-full justify-between py-2">
                <TabsTrigger value="allmails">
                  All Mails
                </TabsTrigger>
                <TabsTrigger value="sent">Sent</TabsTrigger>
                <TabsTrigger value="received">Received</TabsTrigger>
                <TabsTrigger value="web3toweb2">Web3 to Web2</TabsTrigger>
              </TabsList>
              <TabsContent value="allmails">All Mails</TabsContent>
              <TabsContent value="sent">Sent</TabsContent>
              <TabsContent value="received">Received</TabsContent>
              <TabsContent value="web3toweb2">Web3 to Web2</TabsContent>
            </Tabs>
          </div>
        }

        {sidebarstep === 1 && (
          <Directchat />
        )}

        {sidebarstep === 2 && (
          <Groupchat/>
        )}


      </div>
    </div>
  )
}

export default MailPage
