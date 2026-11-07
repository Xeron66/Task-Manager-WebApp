
document.addEventListener("DOMContentLoaded", function() {

    console.log("Task Manager JS loaded successfully!");

    const taskForm = document.getElementById("taskForm");
    const formError = document.getElementById("formError");

    // Check whether the form exists
    if (!taskForm) {
        console.error("Task form not found!");
        return;
    }

    console.log("Task form found. Event listener attached.");

    taskForm.addEventListener("submit", async function(event) {

        // Stop normal browser form submission
        event.preventDefault();

        console.log("Form submission intercepted!");

        // Clear previous errors
        formError.textContent = "";
        formError.classList.add("hidden");

        const submitButton = taskForm.querySelector(
            'button[type="submit"]'
        );

        submitButton.disabled = true;
        submitButton.textContent = "Saving...";

        try {

            const formData = new FormData(taskForm);

            const response = await fetch(taskForm.action, {
                method: "POST",
                body: formData
            });

            const data = await response.json();

            if (!response.ok) {

                formError.textContent = data.error;
                formError.classList.remove("hidden");

                return;
            }

            if (data.success) {
                window.location.href = window.location.pathname;
            }

        } catch (error) {

            console.error("Submission error:", error);

            formError.textContent =
                "Something went wrong. Please try again.";

            formError.classList.remove("hidden");

        } finally {

            submitButton.disabled = false;
            submitButton.textContent = "Save Task";

        }

    });

});


function openModal() {
    const modal = document.getElementById("taskModal");

    modal.classList.remove("hidden");
    modal.classList.add("flex");
}


function closeModal() {
    const modal = document.getElementById("taskModal");

    modal.classList.remove("flex");
    modal.classList.add("hidden");
}
