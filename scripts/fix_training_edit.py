from pathlib import Path
import re

path = Path('/home/ubuntu/extra-fitness-vip/client/src/App.tsx')
text = path.read_text()
pattern = r'function TrainingPage\(\) \{.*?\nconst gallery ='
replacement = '''function TrainingPage() { return <Shell><SEO title="Training | Extra Fitness VIP" description="Explore strength, cardio, functional training and general fitness at Extra Fitness VIP in Sahloul, Sousse." /><InnerHero label="Training areas" title={<>Find what<br /><em>moves you.</em></>} copy="Whatever your goal, make the session count. Explore the ways to train at Extra Fitness VIP." image={img.strength} /><section className="section training-list training-page"><div className="container"><div className="training-list__intro"><Label>Choose your focus</Label><p className="lead">Different goals. One standard: a better version of you.</p></div>{training.map((item) => <article className="training-row" key={item.no}><div className="training-row__meta">{item.no}</div><div className="training-row__image"><img src={item.image} alt={`${item.title} training`} loading="lazy" /></div><div className="training-row__copy"><h2>{item.title}</h2><p>{item.text}</p><span /></div></article>)}</div></section><section className="section section--lime training-note training-page"><div className="container training-note__inner"><Sparkles size={25} /><div><Label>Not sure where to start?</Label><h2>Bring your goal.<br /><span>We’ll bring the energy.</span></h2></div><Link href="/contact" className="button button--dark">Talk to us <ArrowUpRight size={16} /></Link></div></section></Shell>; }
const gallery ='''
new_text, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f'Expected one TrainingPage block, found {count}')
path.write_text(new_text)

css = Path('/home/ubuntu/extra-fitness-vip/client/src/index.css')
styles = css.read_text()
needle = '.training-list { background:var(--paper); }'
if '.training-page { background:#e1e0d5; }' not in styles:
    styles = styles.replace(needle, needle + '\n.training-page { background:#e1e0d5; }')
css.write_text(styles)
