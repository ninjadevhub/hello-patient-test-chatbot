"use client";

import { Container } from "@mantine/core";
import Header from "./Header";
import ChatInput from "./ChatInput";
import { useEffect, useState } from "react";
import { Loader } from "lucide-react";
import { fetchMessages, sendMessageAPI } from "../services/api";

interface Chatinterface {
  role: string;
  content: string;
}

export default function Chat() {
  const [loading, setLoading] = useState<boolean>(false);
  const [chats, setChats] = useState<Chatinterface[]>([]);


  useEffect(() => { 
    setLoading(true);
    fetchMessages('john@example.com').then(res => {
      setLoading(false);
      setChats(res);
    }).catch(err => {
      console.error(err);
    });

  }, [])

  const scrollToBottom = () => {
    const element = document.getElementById("bottom-chat");
    if (element) {
      element.scrollIntoView({ behavior: "smooth" });
    }
  };

  const sendMessage = (prompt: string) => {
    setLoading(true);
    setChats((prevChats) => [...(prevChats||[]), { content: prompt, role: "user" }]);
    sendMessageAPI({email:'john@example.com', prompt}).then(res => {
      setChats((prevChats) => [...(prevChats||[]), { content: res.response, role: "assistant" }]);
      setLoading(false);
    })
    scrollToBottom();
  };

  return (
    <Container className="h-screen flex pb-3 flex-col items-center w-full max-w-full justify-between">
      {/* Header */}
      <div className="fixed bg-white top-0 left-0 w-full shadow-md">
        <Header/>
      </div>

      {/* Chat Messages */}
      <div className="w-3/5 pb-6 h-auto flex justify-center overflow-auto">
        <div className="w-3/5 sm:w-full flex flex-col items-end mt-24 pb-5">
          {/* Default Message */}
          {!chats?.length  && (
            <div className="text-4xl font-bold text-center w-full">
              What can I help with?
            </div>
          )}

          {/* Chat Messages */}
          {chats?.map((chat, index) => (
            <div key={index} className="w-full flex flex-col">
              {chat.role =="user"  &&(
              <div className="w-[60%] shadow h-full mt-4 py-4 px-6 rounded-3xl bg-gray-100">
                <span className="break-words leading-6 tracking-wide font-Barlow text-lg font-medium text-gray-600">
                  {chat.content}
                </span>
              </div>)

          }
              {chat.role == "assistant" && (
                <div className="flex w-full text-right tracking-wide flex-col gap-1 mt-8">
                  <span className="break-words leading-6 tracking-wide font-Barlow text-lg font-medium text-gray-700">
                    {chat.content}
                  </span>
                </div>
              )}
            </div>
          ))}

          {/* Loader */}
          {loading && (
            <div className="w-full flex justify-center items-center mt-4">
              <Loader className="animate-spin text-blue-500" size={40} />
            </div>
          )}

          {/* Scroll to Bottom */}
          <div id="bottom-chat" />
        </div>
      </div>

      {/* Chat Input */}
      <div className="w-3/5">
        <ChatInput onSendMessage={sendMessage} />
      </div>
    </Container>
  );
}
