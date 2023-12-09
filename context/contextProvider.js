import { createContext, useState, useContext } from "react";
export const MessageContextdata = createContext(null);

export default function ContextProvider({ children }) {
    const [sidebarstep, setSidebarStep] = useState(0);

    return (
        <MessageContextdata.Provider value={{ sidebarstep, setSidebarStep }}>
            {children}
        </MessageContextdata.Provider>
    );
}

export const useMessage = () => {
    const context = useContext(MessageContextdata);
    if (!context) {
        throw new Error('useMessage must be used within a MessageProvider');
    }
    return context;
};
