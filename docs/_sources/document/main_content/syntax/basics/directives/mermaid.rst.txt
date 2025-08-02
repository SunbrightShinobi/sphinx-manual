:orphan:

------------------------------------------------
Sphinx Diagram Directives (Mermaid Diagrams)
------------------------------------------------

*   Requirements:

    * Install: mermaid-python via Python :program:`pip` 
    * Install: ``sphinxcontrib-mermaid`` extension via Python :program:`pip`
    * Add ``sphinxcontrib-mermaid`` to Sphinx extensions in conf.py (Included in `SPHINX_ENV_INSTALL`, Sphinx Environment via defaults.py)
    * Configure extension in 'conf.py' like shown below:

        .. code-block:: python

            # sphinxcontrib.mermaid configuration settings
            mermaid_enable = True
            mermaid_output_format = "raw"  # svg, png, pdf
            mermaid_latex_output_format = "pdf"  # pdf is the only option for LaTeX
            mermaid_default_export_scale = 75  # Default scale for exported diagrams
            mermaid_include_elk = "0.1.4" #Include ELK for layout algorithms
            mermaid_cmd = "npx mmdc"
            mermaid_d3_zoom = True  # Enable D3 zoom functionality for Mermaid diagrams

* Flow Diagram

    * Syntax

    .. code-block::

        .. mermaid::
            :name: flowchart_example
            :align: center
            :caption: flowchart_example

            flowchart TD
                A[Christmas] -->|Get money| B(Go shopping)
                B --> C{Let me think}
                C -->|One| D[Laptop]
                C -->|Two| E[iPhone]
                C -->|Three| F[fa:fa-car Car]

    * Rendered

    .. mermaid::
        :name: flowchart_example
        :align: center
        :caption: flowchart_example

        flowchart TD
            A[Christmas] -->|Get money| B(Go shopping)
            B --> C{Let me think}
            C -->|One| D[Laptop]
            C -->|Two| E[iPhone]
            C -->|Three| F[fa:fa-car Car]

* Sequence Diagram

    * Syntax

    .. code-block::

        .. mermaid::
            :name: sequence_diagram_example
            :align: center
            :caption: sequence_diagram_example

            sequenceDiagram
                Alice->>+John: Hello John, how are you?
                Alice->>+John: John, can you hear me?
                John-->>-Alice: Hi Alice, I can hear you!
                John-->>-Alice: I feel great!

    * Rendered

    .. mermaid::
        :name: sequence_diagram_example
        :align: center
        :caption: sequence_diagram_example

            sequenceDiagram
                Alice->>+John: Hello John, how are you?
                Alice->>+John: John, can you hear me?
                John-->>-Alice: Hi Alice, I can hear you!
                John-->>-Alice: I feel great!

* Class Diagram

    * Syntax

    .. code-block::

        .. mermaid::
            :name: class_diagram_example
            :align: center
            :caption: class_diagram_example

            classDiagram
                Animal <|-- Duck
                Animal <|-- Fish
                Animal <|-- Zebra
                Animal : +int age
                Animal : +String gender
                Animal: +isMammal()
                Animal: +mate()
                class Duck{
                +String beakColor
                +swim()
                +quack()
                }
                class Fish{
                -int sizeInFeet
                -canEat()
                }
                class Zebra{
                +bool is_wild
                +run()
                }

    * Rendered

    .. mermaid::
        :name: class_diagram_example
        :align: center
        :caption: class_diagram_example

        classDiagram
            Animal <|-- Duck
            Animal <|-- Fish
            Animal <|-- Zebra
            Animal : +int age
            Animal : +String gender
            Animal: +isMammal()
            Animal: +mate()
            class Duck{
            +String beakColor
            +swim()
            +quack()
            }
            class Fish{
            -int sizeInFeet
            -canEat()
            }
            class Zebra{
            +bool is_wild
            +run()
            }

* State Diagram

    * Syntax

    .. code-block::

        .. mermaid::
            :name: state_diagram_example
            :align: center
            :caption: state_diagram_example

            stateDiagram-v2
                [*] --> Still
                Still --> [*]
                Still --> Moving
                Moving --> Still
                Moving --> Crash
                Crash --> [*]

    * Rendered

    .. mermaid::
        :name: state_diagram_example
        :align: center
        :caption: state_diagram_example

        stateDiagram-v2
            [*] --> Still
            Still --> [*]
            Still --> Moving
            Moving --> Still
            Moving --> Crash
            Crash --> [*]
       
* ER Diagram

    * Syntax

    .. code-block::

        .. mermaid::
            :name: er_diagram_example
            :align: center
            :caption: er_diagram_example

            erDiagram
                CUSTOMER }|..|{ DELIVERY-ADDRESS : has
                CUSTOMER ||--o{ ORDER : places
                CUSTOMER ||--o{ INVOICE : "liable for"
                DELIVERY-ADDRESS ||--o{ ORDER : receives
                INVOICE ||--|{ ORDER : covers
                ORDER ||--|{ ORDER-ITEM : includes
                PRODUCT-CATEGORY ||--|{ PRODUCT : contains
                PRODUCT ||--o{ ORDER-ITEM : "ordered in"

    * Rendered

    .. mermaid::
        :name: er_diagram_example
        :align: center
        :caption: er_diagram_example

        erDiagram
            CUSTOMER }|..|{ DELIVERY-ADDRESS : has
            CUSTOMER ||--o{ ORDER : places
            CUSTOMER ||--o{ INVOICE : "liable for"
            DELIVERY-ADDRESS ||--o{ ORDER : receives
            INVOICE ||--|{ ORDER : covers
            ORDER ||--|{ ORDER-ITEM : includes
            PRODUCT-CATEGORY ||--|{ PRODUCT : contains
            PRODUCT ||--o{ ORDER-ITEM : "ordered in"

  * Gantt Chart

    * Syntax

    .. code-block::

        .. mermaid::
            :name: gantt_chart_example
            :align: center
            :caption: gantt_chart_example

            gantt
                title A Gantt Diagram
                dateFormat  YYYY-MM-DD
                section Section
                A task           :a1, 2014-01-01, 30d
                Another task     :after a1  , 20d
                section Another
                Task in sec      :2014-01-12  , 12d
                another task      : 24d

    * Rendered

    .. mermaid::
        :name: gantt_chart_example
        :align: center
        :caption: gantt_chart_example

        gantt
            title A Gantt Diagram
            dateFormat  YYYY-MM-DD
            section Section
            A task           :a1, 2014-01-01, 30d
            Another task     :after a1  , 20d
            section Another
            Task in sec      :2014-01-12  , 12d
            another task      : 24d

* Journey Diagram

  * Syntax

  .. code-block::

      .. mermaid::
          :name: journey_diagram_example
          :align: center
          :caption: journey_diagram_example

          journey
              title My working day
              section Go to work
              Make tea: 5: Me
              Go upstairs: 3: Me
              Do work: 1: Me, Cat
              section Go home
              Go downstairs: 5: Me
              Sit down: 3: Me

  * Rendered

  .. mermaid::
      :name: journey_diagram_example
      :align: center
      :caption: journey_diagram_example

      journey
          title My working day
          section Go to work
          Make tea: 5: Me
          Go upstairs: 3: Me
          Do work: 1: Me, Cat
          section Go home
          Go downstairs: 5: Me
          Sit down: 3: Me

* Git Graph

  * Syntax

  .. code-block::

      .. mermaid::
          :name: git_graph_example
          :align: center
          :caption: git_graph_example

          gitGraph
              commit
              commit
              branch develop
              checkout develop
              commit
              commit
              checkout main
              merge develop
              commit
              commit
    
  * Rendered

  .. mermaid::
      :name: git_graph_example
      :align: center
      :caption: git_graph_example

      gitGraph
          commit
          commit
          branch develop
          checkout develop
          commit
          commit
          checkout main
          merge develop
          commit
          commit

* Pie Chart

  * Syntax

  .. code-block::

      .. mermaid::
          :name: pie_chart_example
          :align: center
          :caption: pie_chart_example

          pie title Pets adopted by volunteers
              "Dogs" : 386
              "Cats" : 85
              "Rats" : 15

  * Rendered

  .. mermaid::
      :name: pie_chart_example
      :align: center
      :caption: pie_chart_example

      pie title Pets adopted by volunteers
          "Dogs" : 386
          "Cats" : 85
          "Rats" : 15

* Mind Map

  * Syntax

  .. code-block::

      .. mermaid::
          :name: mind_map_example
          :align: center
          :caption: mind_map_example

          mindmap
          root((mindmap))
              Origins
              Long history
              ::icon(fa fa-book)
              Popularisation
                  British popular psychology author Tony Buzan
              Research
              On effectiveness<br/>and features
              On Automatic creation
                  Uses
                      Creative techniques
                      Strategic planning
                      Argument mapping
              Tools
              Pen and paper
              Mermaid

  * Rendered

  .. mermaid::
      :name: mind_map_example
      :align: center
      :caption: mind_map_example

      mindmap
      root((mindmap))
          Origins
          Long history
          ::icon(fa fa-book)
          Popularisation
              British popular psychology author Tony Buzan
          Research
          On effectiveness<br/>and features
          On Automatic creation
              Uses
                  Creative techniques
                  Strategic planning
                  Argument mapping
          Tools
          Pen and paper
          Mermaid

.. * ZenUML   #Not supported in mermaid-python

  * Syntax

  .. code-block::

      .. mermaid::
          :name: zenuml_example
          :align: center
          :caption: zenuml_example

      zenuml
          title Order Service
          @Actor Client #FFEBE6
          @Boundary OrderController #0747A6
          @EC2 <<BFF>> OrderService #E3FCEF
          group BusinessService {
            @Lambda PurchaseService
            @AzureFunction InvoiceService
          }

          @Starter(Client)
          // `POST /orders`
          OrderController.post(payload) {
            OrderService.create(payload) {
              order = new Order(payload)
              if(order != null) {
                par {
                  PurchaseService.createPO(order)
                  InvoiceService.createInvoice(order)      
                }      
              }
            }
          }
    
  * Rendered

  .. mermaid::
      :name: zenuml_example
      :align: center
      :caption: zenuml_example

      zenuml
          title Order Service
          @Actor Client #FFEBE6
          @Boundary OrderController #0747A6
          @EC2 <<BFF>> OrderService #E3FCEF
          group BusinessService {
            @Lambda PurchaseService
            @AzureFunction InvoiceService
          }

          @Starter(Client)
          // `POST /orders`
          OrderController.post(payload) {
            OrderService.create(payload) {
              order = new Order(payload)
              if(order != null) {
                par {
                  PurchaseService.createPO(order)
                  InvoiceService.createInvoice(order)      
                }      
              }
            }
          }

* Quadrant Chart

  * Syntax

  .. code-block::

      .. mermaid::
          :name: quadrant_chart_example
          :align: center
          :caption: quadrant_chart_example

      quadrantChart
          title Reach and engagement of campaigns
          x-axis Low Reach --> High Reach
          y-axis Low Engagement --> High Engagement
          quadrant-1 We should expand
          quadrant-2 Need to promote
          quadrant-3 Re-evaluate
          quadrant-4 May be improved
          Campaign A: [0.3, 0.6]
          Campaign B: [0.45, 0.23]
          Campaign C: [0.57, 0.69]
          Campaign D: [0.78, 0.34]
          Campaign E: [0.40, 0.34]
          Campaign F: [0.35, 0.78]

  * Rendered

  .. mermaid::
      :name: quadrant_chart_example
      :align: center
      :caption: quadrant_chart_example

      quadrantChart
          title Reach and engagement of campaigns
          x-axis Low Reach --> High Reach
          y-axis Low Engagement --> High Engagement
          quadrant-1 We should expand
          quadrant-2 Need to promote
          quadrant-3 Re-evaluate
          quadrant-4 May be improved
          Campaign A: [0.3, 0.6]
          Campaign B: [0.45, 0.23]
          Campaign C: [0.57, 0.69]
          Campaign D: [0.78, 0.34]
          Campaign E: [0.40, 0.34]
          Campaign F: [0.35, 0.78]

.. * XY Chart  #Not supported in mermaid-python

  * Syntax

  .. code-block::

      .. mermaid::
          :name: xy_chart_example
          :align: center
          :caption: xy_chart_example

      xychart-beta
          title XY Chart Example
          x-axis X Axis Label
          y-axis Y Axis Label
          point A: [1, 2]
          point B: [2, 3]
          point C: [3, 1]
          point D: [4, 4]

  * Rendered

  .. mermaid::
      :name: xy_chart_example
      :align: center
      :caption: xy_chart_example

      xyChart-beta
          title XY Chart Example
          x-axis X Axis Label
          y-axis Y Axis Label
          point A: [1, 2]
          point B: [2, 3]
          point C: [3, 1]
          point D: [4, 4]

.. * Block Diagram  #Not supported in mermaid-python

  * Syntax

  .. code-block::

      .. mermaid::
          :name: block_diagram_example
          :align: center
          :caption: block_diagram_example

      block-beta
          title Block Diagram Example
          block A: [0, 0, 100, 100]
          block B: [150, 50, 100, 100]
          block C: [300, 0, 100, 100]
          A --> B
          B --> C

  * Rendered

  .. mermaid::
      :name: block_diagram_example
      :align: center
      :caption: block_diagram_example

      block-beta
          title Block Diagram Example
          block A: [0, 0, 100, 100]
          block B: [150, 50, 100, 100]
          block C: [300, 0, 100, 100]
          A --> B
          B --> C

* Packet

  * Syntax

  .. code-block::

      .. mermaid::
          :name: packet_example
          :align: center
          :caption: packet_example

          ---
          title: "TCP Packet"
          ---
          packet-beta
          0-15: "Source Port"
          16-31: "Destination Port"
          32-63: "Sequence Number"
          64-95: "Acknowledgment Number"
          96-99: "Data Offset"
          100-105: "Reserved"
          106: "URG"
          107: "ACK"
          108: "PSH"
          109: "RST"
          110: "SYN"
          111: "FIN"
          112-127: "Window"
          128-143: "Checksum"
          144-159: "Urgent Pointer"
          160-191: "(Options and Padding)"
          192-255: "Data (variable length)"

  * Rendered

    .. mermaid::
        :name: packet_example
        :align: center
        :caption: packet_example

        ---
        title: "TCP Packet"
        ---
        packet-beta
        0-15: "Source Port"
        16-31: "Destination Port"
        32-63: "Sequence Number"
        64-95: "Acknowledgment Number"
        96-99: "Data Offset"
        100-105: "Reserved"
        106: "URG"
        107: "ACK"
        108: "PSH"
        109: "RST"
        110: "SYN"
        111: "FIN"
        112-127: "Window"
        128-143: "Checksum"
        144-159: "Urgent Pointer"
        160-191: "(Options and Padding)"
        192-255: "Data (variable length)"

.. * TreeMap  #Not supported in mermaid-python

  * Syntax

  .. code-block::

      .. mermaid::
          :name: treemap_example
          :align: center
          :caption: treemap_example

          treemap-beta
          "Section 1"
              "Leaf 1.1": 12
              "Section 1.2"
              "Leaf 1.2.1": 12
          "Section 2"
              "Leaf 2.1": 20
              "Leaf 2.2": 25

  * Rendered

  .. mermaid::
      :name: treemap_example
      :align: center
      :caption: treemap_example

      treemap-beta
      "Section 1"
          "Leaf 1.1": 12
          "Section 1.2"
          "Leaf 1.2.1": 12
      "Section 2"
          "Leaf 2.1": 20
          "Leaf 2.2": 25