import React from 'react'
import Usermsgbox from '../ui/usermsgbox';

function directchat() {

    return (
        <div className='flex flex-col gap-2 w-full'>
            <Usermsgbox />
            <Usermsgbox />
        </div>
    )
}

export default directchat
