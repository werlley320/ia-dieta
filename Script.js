document.getElementById("formulario").addEventListener("submit", async function (e) {
    e.preventDefault();

    const nome = document.getElementById("nome").value;
    const idade = document.getElementById("idade").value;
    const peso = document.getElementById("peso").value;
    const altura = document.getElementById("altura").value;
    const objetivo = document.getElementById("objetivo").value;

    const prompt = `Crie um plano alimentar diário para uma pessoa chamada ${nome}, com ${idade} anos, ${peso}kg, ${altura}cm, cujo objetivo é ${objetivo}. Seja detalhado e inclua café da manhã, almoço, jantar e lanches.`;

    const resultadoDiv = document.getElementById("resultado");
    resultadoDiv.innerHTML = "Gerando plano com IA...";

    try {
        const resposta = await fetch("https://api.openai.com/v1/chat/completions", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer YOUR_API_KEY"
            },
            body: JSON.stringify({
                model: "gpt-3.5-turbo",
                messages: [{ role: "user", content: prompt }],
                temperature: 0.7
            })
        });

        const data = await resposta.json();
        const plano = data.choices[0].message.content;

        resultadoDiv.innerHTML = `<pre>${plano}</pre>`;
    } catch (error) {
        resultadoDiv.innerHTML = "Erro ao gerar plano. Verifique sua conexão ou chave da API.";
        console.error(error);
    }
});
