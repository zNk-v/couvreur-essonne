"""Génère les pages du site à partir de _gabarit/page.html.

Une page par groupe d'annonces Google Ads : le titre, l'accroche et le projet
présélectionné reprennent ce que le visiteur a cherché. Modifier le gabarit ou
les textes ci-dessous, puis lancer depuis la racine du dépôt :

    python3 _gabarit/generer.py

Jekyll (GitHub Pages) ignore les dossiers qui commencent par « _ » : ce
dossier n'est pas publié.
"""

from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent

# Libellé de la conversion Google Ads « Clic téléphone site » (type « Clics sur
# votre numéro sur votre site Web mobile »), commun aux deux sites.
LIBELLE_APPEL = "jnZbCI6m0Z4dEOvMiPdE"
GABARIT = (RACINE / "_gabarit" / "page.html").read_text(encoding="utf-8")

# Réponse commune à toutes les pages : qui rappelle le visiteur.
QUI_RAPPELLE = (
    "Qui va me rappeler ?",
    "Un couvreur partenaire installé en Essonne. Couvreur Essonne est un service gratuit "
    "de mise en relation édité par Sitaly : nous transmettons votre demande à un couvreur "
    "de votre secteur, qui nous rémunère pour ce service. Vous ne payez rien pour le devis.",
)

PAGES = [
    {
        "chemin": "/",
        "lien": "Tous travaux de toiture",
        "titre": "Couvreur en Essonne : fuite, réparation et rénovation de toiture | Couvreur Essonne",
        "description": "Fuite, tuiles cassées, faîtage, zinguerie, rénovation de toiture dans toute l'Essonne (91). Un couvreur local vous rappelle dans la journée. Devis gratuit.",
        "h1": 'Fuite, réparation et rénovation de toiture <span class="accent">en Essonne</span>',
        "sous_titre": "Fuite, tuiles cassées, faîtage descellé, gouttière percée : un couvreur de votre secteur vous rappelle dans la journée. Toiture à refaire ? Il passe aussi chiffrer la rénovation, gratuitement.",
        "titre_form": "Être rappelé dans la journée",
        "exemple_projet": "Ex. : tuiles déplacées après le coup de vent, gouttière qui déborde…",
        "titre_faq": "Réparation de toiture : vos questions",
        "faq": [
            ("Le couvreur se déplace-t-il pour une petite réparation ?",
             "Oui. Une tuile cassée, un faîtage à resceller ou une gouttière qui fuit : il prend tous les travaux, pas seulement les grosses rénovations."),
            ("Sous quel délai suis-je rappelé ?",
             "Dans la journée. Pour une fuite active, appelez directement le 06 58 68 33 72."),
            ("Réparer ou refaire ma toiture ?",
             "Une fuite isolée ou quelques tuiles se réparent. Tuiles poreuses, fuites à répétition, toiture de plus de 40 ans : la rénovation devient plus rentable. Le couvreur monte sur le toit et vous le dit franchement, photos à l'appui."),
            ("Le devis est-il gratuit ?",
             "Oui. La visite et le devis sont gratuits et sans engagement : vous ne payez rien si vous refusez."),
            ("Le couvreur est-il assuré ?",
             "Oui. Le couvreur partenaire a une assurance décennale et une RC Pro : il vous remet ses attestations avec le devis, avant le début des travaux."),
            QUI_RAPPELLE,
        ],
    },
    {
        "chemin": "/couvreur-essonne/",
        "lien": "Couvreur en Essonne",
        "titre": "Couvreur en Essonne (91) : devis gratuit | Couvreur Essonne",
        "description": "Un couvreur installé dans le 91 pour tous vos travaux de toiture : fuite, réparation, zinguerie, rénovation. Rappel dans la journée, devis gratuit.",
        "h1": 'Un couvreur <span class="accent">en Essonne</span>, près de chez vous',
        "sous_titre": "Fuite, réparation, zinguerie, rénovation : tous les travaux de toiture. Un couvreur installé dans le 91 vous rappelle dans la journée et vous remet un devis gratuit.",
        "titre_form": "Demandez votre devis gratuit",
        "exemple_projet": "Ex. : maison à Brétigny, tuiles déplacées après le dernier coup de vent, nous voulons un devis…",
        "titre_faq": "Trouver un couvreur en Essonne : vos questions",
        "faq": [
            ("Dans quelles communes le couvreur intervient-il ?",
             "Dans tout le département de l'Essonne (91) : Évry-Courcouronnes, Massy, Palaiseau, Brétigny-sur-Orge, Savigny-sur-Orge, Corbeil-Essonnes, Étampes et les communes alentour."),
            ("Comment choisir un bon couvreur ?",
             "Demandez l'attestation d'assurance décennale, un devis écrit et détaillé poste par poste, et des photos de votre toiture avant et après. Le couvreur partenaire fournit les trois."),
            ("Le devis est-il vraiment gratuit ?",
             "Oui. La visite et le devis sont gratuits et sans engagement : vous ne payez rien si vous refusez."),
            ("Sous quel délai suis-je rappelé ?",
             "Un couvreur vous rappelle dans la journée pour convenir d'une visite."),
            QUI_RAPPELLE,
        ],
    },
    {
        "chemin": "/reparation-fuite-toiture/",
        "lien": "Fuite et réparation de toiture",
        "titre": "Fuite et réparation de toiture en Essonne | Couvreur Essonne",
        "description": "Fuite de toit, infiltration, tuiles cassées, faîtage ou solin abîmé en Essonne (91) : un couvreur local vous rappelle dans la journée. Devis gratuit.",
        "h1": 'Fuite et réparation de toiture <span class="accent">en Essonne</span>',
        "sous_titre": "Infiltration au plafond, tuiles cassées, faîtage ou solin abîmé. Un couvreur de votre secteur vous rappelle dans la journée, cherche l'origine de la fuite et la répare.",
        "titre_form": "Demandez votre devis de réparation",
        "exemple_projet": "Ex. : tache d'humidité au plafond de la chambre depuis les pluies, tuiles déplacées près de la cheminée…",
        "titre_faq": "Fuite de toiture : vos questions",
        "faq": [
            ("D'où vient une fuite de toiture ?",
             "Le plus souvent d'une tuile cassée ou déplacée, d'un faîtage descellé, d'un solin de cheminée fissuré ou d'une gouttière bouchée. L'eau peut ressortir loin de son point d'entrée : le couvreur monte sur le toit pour trouver la vraie cause."),
            ("Que faire en attendant le couvreur ?",
             "Placez un récipient sous la fuite, protégez vos meubles et coupez l'électricité de la pièce si l'eau approche d'un plafonnier. Ne montez pas sur le toit vous-même."),
            ("Réparer ou refaire la toiture ?",
             "Une fuite isolée se répare. Des fuites à répétition sur une toiture ancienne annoncent souvent une réfection. Le couvreur vous le dit franchement, photos à l'appui."),
            ("Mon assurance habitation peut-elle prendre en charge les dégâts ?",
             "Les dégâts des eaux à l'intérieur sont souvent couverts, selon votre contrat. Déclarez le sinistre rapidement et gardez le devis et les photos du couvreur pour votre assureur."),
            QUI_RAPPELLE,
        ],
    },
    {
        "chemin": "/charpente-essonne/",
        "lien": "Rénovation de charpente",
        "titre": "Rénovation de charpente en Essonne | Couvreur Essonne",
        "description": "Charpente abîmée, bois attaqué, toiture qui s'affaisse en Essonne (91) : un couvreur-charpentier local vous remet un devis gratuit après visite.",
        "h1": 'Rénovation de charpente <span class="accent">en Essonne</span>',
        "sous_titre": "Bois attaqué par les insectes ou l'humidité, pièces qui fléchissent, toiture qui s'affaisse. Un couvreur-charpentier de votre secteur vous rappelle et passe chiffrer gratuitement.",
        "titre_form": "Demandez votre devis de charpente",
        "exemple_projet": "Ex. : maison ancienne, chevrons qui fléchissent, le faîtage fait une bosse, nous voulons un diagnostic…",
        "titre_faq": "Charpente : vos questions",
        "faq": [
            ("Comment savoir si ma charpente est abîmée ?",
             "Toiture qui ondule ou s'affaisse, bois qui s'effrite, sciure ou petits trous dans les combles, traces d'humidité sur les chevrons. Au moindre doute, une visite permet de vérifier pièce par pièce."),
            ("Faut-il changer toute la charpente ?",
             "Rarement. Le plus souvent, on remplace ou renforce les pièces abîmées et on traite le bois. Le couvreur vous explique ce qu'il garde et ce qu'il change."),
            ("Peut-on rénover la charpente en même temps que la toiture ?",
             "C'est le meilleur moment : la couverture est déposée, la charpente est accessible. Vous ne payez l'échafaudage qu'une fois."),
            ("La charpente est-elle couverte par l'assurance décennale ?",
             "Oui, les travaux de charpente entrent dans l'assurance décennale du couvreur partenaire. Il vous remet son attestation avec le devis."),
            QUI_RAPPELLE,
        ],
    },
    {
        "chemin": "/devis-toiture/",
        "lien": "Rénovation de toiture",
        "titre": "Rénovation de toiture en Essonne : devis gratuit | Couvreur Essonne",
        "description": "Rénovation, réfection ou démoussage de toiture en Essonne (91) : un couvreur local passe voir votre toit et vous remet un devis gratuit et détaillé.",
        "h1": 'Rénovation de toiture <span class="accent">en Essonne</span>',
        "sous_titre": "Tuiles poreuses, mousse, fuites à répétition : un couvreur de votre secteur vous rappelle dans la journée, passe voir la toiture et vous dit s'il faut réparer ou refaire.",
        "titre_form": "Demandez votre devis de rénovation",
        "exemple_projet": "Ex. : toiture des années 70, tuiles poreuses, on hésite entre démoussage et réfection…",
        "titre_faq": "Rénovation et devis toiture : vos questions",
        "faq": [
            ("Que contient le devis ?",
             "Chaque poste chiffré après visite : dépose, charpente, écran sous-toiture, liteaunage, couverture, zinguerie, échafaudage et évacuation des gravats. Vous savez exactement ce que vous payez."),
            ("Le devis est-il gratuit et sans engagement ?",
             "Oui. La visite et le devis sont gratuits. Vous ne payez rien si vous refusez."),
            ("Pourquoi une visite avant le devis ?",
             "Une toiture ne se chiffre pas sur photo : l'état de la charpente, l'accès et les points singuliers (cheminée, noues, fenêtres de toit) changent le prix. La visite évite les mauvaises surprises en cours de chantier."),
            ("Sous quel délai ai-je mon devis ?",
             "Un couvreur vous rappelle dans la journée pour fixer la visite, puis vous envoie le devis écrit."),
            QUI_RAPPELLE,
        ],
    },
]


def faq_html(questions):
    return "\n".join(
        f"        <details><summary>{q}</summary><p>{r}</p></details>" for q, r in questions
    )


def liens_html(page):
    return "\n".join(
        f'        <li><a href="{p["chemin"]}">{p["lien"]}</a></li>'
        for p in PAGES
        if p["chemin"] != page["chemin"]
    )


def generer(page):
    html = GABARIT
    valeurs = dict(page, faq=faq_html(page["faq"]), autres_pages=liens_html(page), libelle_appel=LIBELLE_APPEL)
    for cle, valeur in valeurs.items():
        if isinstance(valeur, str):
            html = html.replace("{{" + cle + "}}", valeur)
    reste = [m for m in ("{{",) if m in html]
    if reste:
        raise SystemExit(f"Variable non remplacée dans {page['chemin']}")
    sortie = RACINE / page["chemin"].strip("/") / "index.html"
    sortie.parent.mkdir(parents=True, exist_ok=True)
    sortie.write_text(html, encoding="utf-8")
    print(f"{page['chemin']:<30} → {sortie.relative_to(RACINE)}")


if __name__ == "__main__":
    for page in PAGES:
        generer(page)
