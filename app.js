<script>
  $(document).ready(function() {
    $('#register-form').on('submit', function (e) {
      e.preventDefault();
      var formData = {
        firstname: $('#firstname').val(),
        lastname: $('#lastname').val(),
        username: $('#username').val(),
        email: $('#email').val(),
        phone_number: $('#phone').val(),
        location: $('#location').val(),
        role: $('#role').val(),
        password: $('#password').val()
      };

      $.ajax({
        type: 'POST',
        url: 'https://your-backend-domain.com/api/register', // Replace with your backend API endpoint
        contentType: 'application/json',
        data: JSON.stringify(formData),
        success: function (response) {
          alert('Registration successful! Please log in.');
          window.location.href = 'login.html'; // Redirect to login page
        },
        error: function (error) {
          alert('Error: ' + error.responseText);
        }
      });
    });
        });
</script>