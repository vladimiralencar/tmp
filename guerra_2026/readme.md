# Wave-Level Strike Dataset

## Visão Geral

O **Wave-Level Strike Dataset** é um conjunto de dados estruturado em nível de *onda de ataque* (*wave-level*), no qual cada linha representa uma onda específica dentro de uma operação militar mais ampla.

O objetivo do dataset é fornecer uma base estruturada para **análise temporal, operacional e estratégica de campanhas de ataques**, permitindo estudos quantitativos sobre padrões de operações, composição de armamentos e dinâmica temporal entre ondas.

O dataset integra **metadados temporais, identificadores operacionais, composição de armamentos e indicadores de sistemas de armas**, permitindo análises em áreas como:

* modelagem de ritmo operacional (*operational tempo*)
* análise de sequenciamento de ondas
* padrões de uso de sistemas de armas
* análise temporal de campanhas militares
* comparação entre operações diurnas e noturnas

O dataset foi projetado para uso em **pesquisa acadêmica, análise OSINT, ciência de dados aplicada a conflitos e modelagem de eventos**.

---

# Estrutura do Dataset

Cada linha do dataset representa **uma onda de ataque individual** dentro de uma operação.

Identificador primário:

```
wave_uid
```

Exemplo de registro:

```
wave_uid: tp4_w21
operation: tp4
wave_number: 21
probable_launch_time: 2026-02-15T21:10:00Z
drones_used: true
ballistic_missiles_used: true
```

---

# Dicionário de Dados

| Campo                      | Tipo     | Descrição                                                           |
| -------------------------- | -------- | ------------------------------------------------------------------- |
| wave_uid                   | string   | Identificador único da onda utilizado para junções entre tabelas    |
| operation                  | string   | Identificador da operação (tp1, tp2, tp3, tp4)                      |
| wave_number                | integer  | Número sequencial da onda dentro da operação                        |
| wave_codename_farsi        | string   | Codinome da onda em escrita persa (farsi)                           |
| wave_codename_english      | string   | Codinome da onda transliterado para o inglês                        |
| announced_utc              | datetime | Timestamp em UTC indicando quando a onda foi anunciada ou detectada |
| announcement_source        | string   | Fonte do primeiro anúncio ou detecção                               |
| probable_launch_time       | datetime | Horário estimado de lançamento baseado em análise OSINT             |
| launch_time_israel         | string   | Horário local do lançamento no fuso de Israel                       |
| launch_time_iran           | string   | Horário local do lançamento no fuso do Irã                          |
| solar_phase_launch_site    | integer  | Fase de iluminação solar no local de lançamento                     |
| solar_phase_target         | integer  | Fase de iluminação solar no alvo                                    |
| conflict_day               | integer  | Dia do conflito dentro da operação                                  |
| hours_since_last_wave      | float    | Horas decorridas desde a onda anterior                              |
| time_between_waves_minutes | float    | Minutos decorridos desde a onda anterior                            |
| wave_duration_minutes      | float    | Duração estimada da onda                                            |
| payload                    | string   | Descrição textual da composição do armamento                        |
| drones_used                | boolean  | Indica se drones ou munições vagantes foram usados                  |
| ballistic_missiles_used    | boolean  | Indica se mísseis balísticos foram usados                           |
| cruise_missiles_used       | boolean  | Indica se mísseis de cruzeiro foram usados                          |
| emad_used                  | boolean  | Indica uso do sistema de mísseis Emad                               |
| ghadr_used                 | boolean  | Indica uso do sistema de mísseis Ghadr                              |
| sejjil_used                | boolean  | Indica uso do sistema de mísseis Sejjil                             |
| kheibar_shekan_used        | boolean  | Indica uso do sistema de mísseis Kheibar Shekan                     |

---

# Codificação de Variáveis

## Fase Solar

Valores possíveis para os campos:

* `solar_phase_launch_site`
* `solar_phase_target`

```
0 = Noite
1 = Crepúsculo astronômico
2 = Crepúsculo náutico
3 = Crepúsculo civil
4 = Sol baixo
5 = Luz do dia
```

---

# Possíveis Aplicações

Este dataset pode ser utilizado em diversos tipos de análise:

### Pesquisa acadêmica

* estudos de segurança internacional
* análise quantitativa de conflitos
* modelagem de eventos militares

### Ciência de dados

* análise de séries temporais
* modelagem de eventos sequenciais
* detecção de padrões operacionais

### Machine Learning

* previsão de eventos
* classificação de ondas
* detecção de anomalias em ritmo operacional

---

# Fontes de Dados

O dataset é baseado em informações derivadas de:

* monitoramento OSINT
* anúncios oficiais
* reconstrução temporal baseada em evidências abertas
* relatórios públicos de eventos relacionados ao conflito

Alguns campos podem representar **estimativas analíticas quando dados diretos não estavam disponíveis**.

---

# Limitações

Algumas limitações devem ser consideradas:

* determinados horários podem ser **estimativas baseadas em reconstrução analítica**
* composição de armamentos pode refletir **melhor avaliação OSINT disponível**
* algumas ondas podem ter **dados incompletos devido a lacunas de reporte**

---

# Considerações Éticas

Este dataset contém informações relacionadas a **eventos de conflito militar**.

Seu uso é destinado exclusivamente a:

* pesquisa
* análise acadêmica
* estudos de segurança
* modelagem científica de eventos

Os usuários devem garantir uso responsável e ético dos dados.

---

# Versão do Dataset

```
v1.0
```

---

# Licença

Especifique aqui a licença do dataset.

Exemplos comuns:

* MIT
* CC-BY-4.0
* CC-BY-SA-4.0
* Open Data Commons
