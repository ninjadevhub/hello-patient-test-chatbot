"use client";

import NewChat from "../assets/NewChat";


function Header() {
  return (
    <div className="!py-[20px] !px-8 !mb-1.5 flex items-center justify-between z-10 font-semibold ">
      <div className="flex items-center gap-0 overflow-hidden">
        <NewChat />
      </div>
   
    </div>
  );
}

export default Header;
