import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

# Définir les clés d'API
os.environ["SERPER_API_KEY"] = "YOURAPI"  # clé API de serper.dev
os.environ["OPENAI_API_KEY"] = "YOURAPI"

# Outil de recherche
search_tool = SerperDevTool()

# Créer un expert en growth hacking
growth_expert = Agent(
    role='Expert en Growth Hacking',
    goal='Atteindre un chiffre d\'affaires de 10M€ en vente de formations en ligne en growth hacking',
    verbose=True,
    memory=True,
    backstory=(
        "Avec une expertise approfondie en growth hacking, vous êtes déterminé à maximiser le potentiel de vente des formations en ligne."
    ),
    tools=[search_tool],
    allow_delegation=True
)

# Créer un expert en copywriting
copywriting_expert = Agent(
    role='Expert en Copywriting',
    goal='Créer des contenus captivants et persuasifs pour promouvoir les formations en ligne en growth hacking',
    verbose=True,
    memory=True,
    backstory=(
        "Doté d'un talent exceptionnel pour rédiger des contenus persuasifs, votre objectif est de créer des messages qui incitent à l'action et à l'achat."
    ),
    tools=[search_tool],
    allow_delegation=False
)

# Créer un expert en branding
branding_expert = Agent(
    role='Expert en Branding',
    goal='Développer une image de marque forte et distinctive pour les formations en ligne en growth hacking',
    verbose=True,
    memory=True,
    backstory=(
        "Avec une compréhension approfondie de la psychologie du consommateur, votre mission est de créer une identité de marque qui se démarque et attire les clients potentiels."
    ),
    tools=[search_tool],
    allow_delegation=False
)

# Créer un expert en vente
sales_expert = Agent(
    role='Expert en Vente',
    goal='Maximiser les ventes de formations en ligne en growth hacking grâce à des stratégies de vente efficaces',
    verbose=True,
    memory=True,
    backstory=(
        "Avec une expérience avérée dans la vente, vous êtes déterminé à convaincre les clients potentiels de l'importance et de la valeur des formations en ligne en growth hacking."
    ),
    tools=[search_tool],
    allow_delegation=False
)

# Créer un expert en tunnel de vente
sales_funnel_expert = Agent(
    role='Expert en Tunnel de Vente',
    goal='Optimiser les tunnels de vente pour maximiser les conversions et les revenus des formations en ligne en growth hacking',
    verbose=True,
    memory=True,
    backstory=(
        "Avec une expertise en conception de tunnels de vente, vous êtes chargé de créer des parcours d'achat fluides et efficaces pour transformer les prospects en clients."
    ),
    tools=[search_tool],
    allow_delegation=False
)

# Définir les tâches pour chaque expert
growth_task = Task(
    description=(
        "Identifier les segments de marché les plus prometteurs pour les formations en ligne en growth hacking."
        "Focalisez-vous sur les opportunités de croissance et les stratégies de pénétration du marché."
        "Votre rapport final devrait décrire clairement les segments cibles, leurs besoins et leurs comportements."
    ),
    expected_output='Un rapport complet sur les segments de marché les plus prometteurs.',
    tools=[search_tool],
    agent=growth_expert,
)

copywriting_task = Task(
    description=(
        "Rédiger des copies persuasives pour les pages de vente des formations en ligne en growth hacking."
        "Mettez en évidence les avantages, les témoignages clients et les appels à l'action convaincants."
    ),
    expected_output='Des copies persuasives pour les pages de vente.',
    tools=[search_tool],
    agent=copywriting_expert,
)

branding_task = Task(
    description=(
        "Développer une identité de marque distincte pour les formations en ligne en growth hacking."
        "Incluez le logo, les couleurs, la typographie et la voix de la marque pour renforcer la reconnaissance et la fidélité des clients."
    ),
    expected_output='Une identité de marque complète et distinctive.',
    tools=[search_tool],
    agent=branding_expert,
)

sales_task = Task(
    description=(
        "Mettre en place des stratégies de vente efficaces pour les formations en ligne en growth hacking."
        "Focalisez-vous sur la conversion des prospects en clients payants et l'augmentation des ventes."
    ),
    expected_output='Des stratégies de vente efficaces pour maximiser les conversions.',
    tools=[search_tool],
    agent=sales_expert,
)

sales_funnel_task = Task(
    description=(
        "Optimiser les tunnels de vente pour les formations en ligne en growth hacking."
        "Analysez les étapes du processus d'achat et proposez des améliorations pour augmenter les taux de conversion."
    ),
    expected_output='Des tunnels de vente optimisés pour maximiser les conversions.',
    tools=[search_tool],
    agent=sales_funnel_expert,
)

# Créer l'équipage avec les experts et les tâches associées
crew = Crew(
    agents=[growth_expert, copywriting_expert, branding_expert, sales_expert, sales_funnel_expert],
    tasks=[growth_task, copywriting_task, branding_task, sales_task, sales_funnel_task],
    process=Process.sequential,  # Exécution séquentielle des tâches
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

# Lancer le processus d'exécution des tâches
result = crew.kickoff(inputs={'topic': 'formations en ligne en growth hacking pour réaliser 10M€'})
print(result)
