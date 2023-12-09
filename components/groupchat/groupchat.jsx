import React from 'react'
import Usermsgbox from '../ui/usermsgbox';

function groupchat() {

    return (
        <div className='flex flex-col gap-2 w-full'>
            <Usermsgbox />
            <Usermsgbox />
        </div>
    )
}

export default groupchat
