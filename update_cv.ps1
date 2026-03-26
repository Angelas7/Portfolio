$path = "d:\CV PORTFOLIO\index.html"
$lines = Get-Content $path -Encoding UTF8
$lines[452] = '            <p style="margin-bottom: 20px;">Computer Science student with a focus on Cybersecurity, committed to engineering technology that people and organizations can depend on. Motivated by understanding complex systems end-to-end — their architecture, vulnerabilities, and the strategies required to make them robust in an increasingly hostile digital landscape.</p>'
$lines[453] = '            <p style="margin-bottom: 20px;">Builds software with an emphasis on clarity, scalability, and security, transforming ideas into practical, high-value solutions. Combines strong technical foundations with strategic thinking, continuous learning, and a drive to push beyond conventional limits.</p>'
$lines[454] = '            <p>Aspires to lead the development of secure, intelligent systems that power the future — creating technology that is not only innovative, but responsible, resilient, and built to endure.</p>'
$lines | Set-Content $path -Encoding UTF8
