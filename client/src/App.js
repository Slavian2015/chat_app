import {useState, useEffect} from "react";
import "./App.css";

function App() {
    const [clientId, setClientId] = useState(Math.floor(new Date().getTime() / 1000));
    const [websckt, setWebsckt] = useState();
    const [message, setMessage] = useState([]);
    const [messages, setMessages] = useState([]);

    useEffect(() => {
        const url = "ws://0.0.0.0:8090/ws/" + clientId;
        const ws = new WebSocket(url);

        ws.onopen = event => {
            ws.send("Start");
        };

        ws.onclose = (e) => {
            console.log('close ws connection: ', e.code, e.reason)
        }

        ws.onmessage = (e) => {
            let str = e.data.replaceAll("\"", "&quot;")
            str = e.data.replaceAll("'", "\"");
            setMessages(prevMessages => [...prevMessages, JSON.parse(str)]);
        };

        setWebsckt(ws);
        return () => ws.close();
    }, []);

    const sendMessage = () => {
        websckt.send(message);
        setMessages(prevMessages => [...prevMessages, {sender:clientId, message: message}]);
        setMessage([]);
        console.log("sendMessage messages", messages)
    };

    return (
        <div className="container">
            <h1>Chat</h1>
            <h2>Your client id: {clientId} </h2>
            <div className="chat-container">
                <div className="chat">
                    {messages.map((value, index) => {
                        if (value.sender === clientId) {
                            return (
                                <div key={index} className="my-message-container">
                                    <div className="my-message">
                                        <p className="client">client id : {clientId}</p>
                                        <p className="message">{value.message}</p>
                                    </div>
                                </div>
                            );
                        } else {
                            return (
                                <div key={index} className="another-message-container">
                                    <div className="another-message">
                                        <p className="client">Server</p>
                                        <p className="message">{value.message}</p>
                                    </div>
                                </div>
                            );
                        }
                    })}
                </div>
                <div className="input-chat-container">
                    <input
                        className="input-chat"
                        type="text"
                        placeholder="Chat message ..."
                        onChange={e => setMessage(e.target.value)}
                        onKeyDown={e => {
                            if (e.code === 'Enter') {
                                sendMessage()
                            }
                        }}
                        value={message}
                    ></input>
                    <button className="submit-chat" onClick={sendMessage}>
                        Send
                    </button>
                </div>
            </div>
        </div>
    );
}

export default App;
