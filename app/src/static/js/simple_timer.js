let i = 9;
document.addEventListener('DOMContentLoaded', setInterval(() => {
  const element = document.querySelector("#coutdown>p");
  if (i >= 0){
    element.innerHTML = `<p>Redirecting in ${i--}</p>`
  } else{
    window.location.href = "{{url_for('auth.login')}}"
  };
}, 1000));