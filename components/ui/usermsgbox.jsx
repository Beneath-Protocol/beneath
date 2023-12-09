import Image from "next/image";
import chat from "../directchat/chat";

const Usermsgbox = ({ image, msg, time }) => {
    return (
        <div  className="rounded-lg items-center border-2 border-gray-100 flex justify-between p-2 text-white hover:cursor-pointer">
            <div className="flex gap-4">
                <Image className="w-8 h-8 rounded-full" src={image} alt="profile"></Image>
                <div>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Harum necessitatibus quaerat odit!</div>
            </div>
            <div>17:45</div>
        </div>
    );
}

export default Usermsgbox;