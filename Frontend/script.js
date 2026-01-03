document.getElementById("generateBtn").addEventListener("click", function () {
    let text = document.getElementById("qrText").value;
    if (text.trim() === "") {
        alert("Please enter some text!");
        return;
    }

    let qrImage = document.getElementById("qrImage");
    let downloadBtn = document.getElementById("downloadBtn");

    // ✅ Relative API call (works locally & on EC2)
    fetch(`/generate_qr?data=${encodeURIComponent(text)}`)
        .then(response => response.blob())
        .then(blob => {
            let imageUrl = URL.createObjectURL(blob);
            qrImage.src = imageUrl;
            qrImage.style.display = "block";

            downloadBtn.href = imageUrl;
            downloadBtn.style.display = "inline-block";
        })
        .catch(error => console.error("Error:", error));
});
