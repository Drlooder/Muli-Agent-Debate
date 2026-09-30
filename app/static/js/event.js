const socket = io()

document.getElementById("prompt_form").addEventListener("submit", function(e){
    e.preventDefault()

    const prompt_value = document.getElementById("topic-input").value;

    socket.emit("send_prompt", {prompt: prompt_value})
})

socket.on("prompt_response", function(data) {
    const generated_response = data.generated_response
    
})