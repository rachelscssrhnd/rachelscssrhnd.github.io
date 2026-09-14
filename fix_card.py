content = open('index.html', 'r', encoding='utf-8').read()

old = (
    '    <p>Additional infographic projects including Smart Living di IKN: Inovasi dalam Kesehatan, '
    'Kesejahteraan, dan Keselamatan Publik melalui Data dan Statistik; Green Commerce: How Data Science '
    'Drives Environmental Sustainability in E-Commerce; Smart Farming; and Youth Transforming Manufacturing: '
    'Unlocking The Power of AI and Digital Integration are available on '
    '<a href="https://github.com/rachelscssrhnd/Graphic-Design-Portfolio" target="_blank" rel="noopener">'
    'GitHub</a>.</p>\n  </section>'
)

new = (
    '    <h3>Other Infographic &amp; Visual Storytelling Projects</h3>\n'
    '    <p class="project-role">National Competitions &amp; Design Portfolio</p>\n'
    '    <p>Additional data-driven infographics and visual storytelling projects submitted to national competitions, '
    'including Smart Living di IKN: Inovasi dalam Kesehatan, Kesejahteraan, dan Keselamatan Publik melalui Data dan Statistik; '
    'Green Commerce: How Data Science Drives Environmental Sustainability in E-Commerce; Smart Farming; '
    'and Youth Transforming Manufacturing: Unlocking The Power of AI and Digital Integration in ASEAN.</p>\n'
    '    <p><a href="https://github.com/rachelscssrhnd/Graphic-Design-Portfolio" target="_blank" rel="noopener">View Project</a></p>\n'
    '  </section>'
)

if old in content:
    content = content.replace(old, new)
    open('index.html', 'w', encoding='utf-8').write(content)
    print('SUCCESS')
else:
    print('NOT FOUND')
    print(repr(content[content.find('Additional infographic'):content.find('Additional infographic')+300]))
