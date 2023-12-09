import React from 'react'
import { useState, useEffect } from 'react';

function chat({}) {
    const [message, setMessage] = useState('');
    const [messages, setMessages] = useState([]);
    const [renderMessages, setRenderMessages] = useState([]);
    const [processing, setProcessing] = useState(false);
    // const [isSpinning, setIsSpinning] = useState(false);
    const [id, setid] = useState('')

    useEffect(() => {
        console.log(messages);
        const newRenderMessages = messages.map((msg, index) => (
            <div key={index} className={`${msg.role === 'user' ? 'text-white flex justify-end w-full my-2' : 'text-white flex justify-start w-full my-2'}`}>
                <div className={`${msg.role === 'user' ? 'bg-green-500 p-2 rounded-md max-w-[80%]' : 'bg-blue-500 p-2 rounded-md max-w-[80%]'}`}>
                    <p>{msg.content}</p>
                </div>
            </div>
        ));
        setRenderMessages(newRenderMessages);
    }, [messages]);

    const sendMessage = async () => {
        
    };

    return (
        <div className="bg-[#373737] max-h-max flex flex-col w-full h-[600px] self-center justify-center rounded-lg border-[1.5px] border-gray-200">
            <div className="p-4 bg-[#1f1e1e] flex justify-between w-full gap-2 items-center rounded-t-lg">
                <div className='flex gap-2 items-center'>
                    <span className='font-bold text-lg'>Lets chat!</span>
                </div>
                {/* <div className='flex'>
                        <div className={`bg-white p-2 rounded-full hover:cursor-pointer shadow-lg shadow-gray-400 ${isSpinning ? 'animate-spin' : ''}`}>
                            <Image onClick={refresh_clicked} className='rounded-full' width={30} height={30} src={Refresh} alt="icon" />
                        </div>
                    </div> */}
            </div>
            <div className=" text-black flex-1 p-4 overflow-y-auto">
                {renderMessages}
                <div className={`${processing === true ? 'text-white flex justify-start w-full my-2' : 'hidden'}`}>
                    <div className={`${processing === true ? 'bg-gray-500 p-2 rounded-md' : 'hidden'}`}>
                        <p>Loading...</p>
                    </div>
                </div>
            </div>
            <div className="p-4 flex flex-col gap-2">
                <textarea
                    id="textarea"
                    className='w-full p-2 rounded-lg'
                    cols="30"
                    rows="2"
                    style={{ resize: 'none' }}
                    placeholder="Write a message..."
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                />
                <button
                    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 w-fit rounded"
                    onClick={() => { sendMessage() }}
                >
                    Send
                </button>
            </div>
        </div>
    )
}

export default chat
