document.addEventListener('DOMContentLoaded', () => {
    const startBtn = document.getElementById('start-btn');
    const stopBtn = document.getElementById('stop-btn');
    const topicInput = document.getElementById('debate-topic');
    const statusBadge = document.getElementById('socket-status');
    const randomTopicBtn = document.getElementById('random-topic-btn');

    const agentStreams = {
        'agent_1': document.getElementById('stream-agent-1'),
        'agent_2': document.getElementById('stream-agent-2'),
        'moderator': document.getElementById('stream-agent-mod')
    };

    const agentCards = {
        'agent_1': document.getElementById('agent-1-card'),
        'agent_2': document.getElementById('agent-2-card'),
        'moderator': document.getElementById('agent-mod-card')
    };

    // Initialize Socket Handler with UI Callbacks
    DebateSocket.init({
        onConnect: () => {
            statusBadge.textContent = 'Connected';
            statusBadge.className = 'connection-badge connected';
        },
        onDisconnect: () => {
            statusBadge.textContent = 'Disconnected';
            statusBadge.className = 'connection-badge disconnected';
            resetUIState();
        },
        onAgentChunk: (data) => {
            handleIncomingChunk(data);
        },
        onDebateEnd: () => {
            resetUIState();
        },
        onError: (data) => {
            console.error('Debate Error:', data.message);
            alert(`Error: ${data.message}`);
            resetUIState();
        },

        onRandomTopic: (data) => {
            topicInput.value = data.topic;
            topicInput.focus();
        },
    });

    startBtn.addEventListener('click', () => {
        const topic = topicInput.value.trim();
        if (!topic) return alert('Please enter a topic.');

        // UI Transition
        startBtn.disabled = true;
        stopBtn.disabled = false;
        clearStreams();

        // Emit socket event
        DebateSocket.startDebate(topic);
    });

    randomTopicBtn.addEventListener("click", () => {
        DebateSocket.GenerateRandomTopic()
    })

    stopBtn.addEventListener('click', () => {
        DebateSocket.stopDebate();
        resetUIState();
    });


    function handleIncomingChunk(data) {
        const { agent, chunk } = data;
        if (agentStreams[agent]) {
            setActiveAgentCard(agent);
            agentStreams[agent].dataset.rawText =
                (agentStreams[agent].dataset.rawText || '') + chunk;
            agentStreams[agent].innerHTML = marked.parse(
                agentStreams[agent].dataset.rawText
            );
            agentStreams[agent].querySelectorAll('pre code').forEach((block) => {
                hljs.highlightElement(block);
            });
            agentStreams[agent].scrollTop =
                agentStreams[agent].scrollHeight;
        }
    }



    function setActiveAgentCard(activeAgent) {
        Object.keys(agentCards).forEach(key => {
            if (key === activeAgent) {
                agentCards[key].classList.add('active');
            } else {
                agentCards[key].classList.remove('active');
            }
        });
    }

    function clearStreams() {
        Object.values(agentStreams).forEach(stream => stream.textContent = '');
    }

    function resetUIState() {
        startBtn.disabled = false;
        stopBtn.disabled = true;
        Object.values(agentCards).forEach(card => card.classList.remove('active'));
    }
});

