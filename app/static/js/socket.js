/**
 * Socket.IO Connection Handler
 */

const randomBtn = document.getElementById("")
const DebateSocket = {
    socket: null,

    init(callbacks) {
        this.socket = io();

        // System Events
        this.socket.on('connect', () => {
            if (callbacks.onConnect) callbacks.onConnect();
        });

        this.socket.on('disconnect', () => {
            if (callbacks.onDisconnect) callbacks.onDisconnect();
        });

        // Custom Debate Events from Flask Backend
        this.socket.on('agent_response', (data) => {
            // Expected data format: { agent: 'agent_1'|'agent_2'|'moderator', chunk: 'string' }
            if (callbacks.onAgentChunk) callbacks.onAgentChunk(data);
        });

        this.socket.on('debate_finished', () => {
            if (callbacks.onDebateEnd) callbacks.onDebateEnd();
        });

        this.socket.on('error_message', (data) => {
            if (callbacks.onError) callbacks.onError(data);
        });

        this.socket.on('generated_topic', (data) => {
            if (callbacks.onRandomTopic) callbacks.onRandomTopic(data);
        })
    },

    startDebate(topic) {
        if (this.socket && this.socket.connected) {
            this.socket.emit('start_debate', { topic: topic });
        }
    },

    stopDebate() {
        if (this.socket && this.socket.connected) {
            this.socket.emit('stop_debate');
        }
    },

    GenerateRandomTopic() {
        if (this.socket && this.socket.connected) {
            this.socket.emit("generate_random_topic")
        }
    }
};