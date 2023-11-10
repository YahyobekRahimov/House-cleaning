import React from "react";
import {ReactComponent as ChatIcon} from '../icons/live-chat.svg';

function LiveChat() {
    return (
        <section class="chatbot">
            <div class="container chatbot__container">
                <button class="live-chat-button">
                    <ChatIcon />
                </button>
            </div>
        </section>
    )
}

export default LiveChat;