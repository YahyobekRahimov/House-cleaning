import React from "react";
import {ReactComponent as ChatIcon} from '../icons/live-chat.svg';

function LiveChat() {
    return (
        <section className="chatbot">
            <div className="container chatbot__container">
                <button className="live-chat-button">
                    <ChatIcon />
                </button>
            </div>
        </section>
    )
}

export default LiveChat;