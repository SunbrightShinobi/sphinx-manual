:orphan:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Sphinx Diagram Directives (PlantUML)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*   Requirements:

    *   Install: ``sphinxcontrib-plantuml`` via Python :program:`pip` (Included in `SPHINX_ENV_INSTALL`, Sphinx Environment)
    *   Copy ``graphviz-2.38`` folder to :file:`/` (Included in `SPHINX_ENV_INSTALL`, Sphinx Environment via install.sh)
    *   Copy ``plantuml.jar`` to :file:`/java` (Included in `SPHINX_ENV_INSTALL`, Sphinx Environment via install.sh)
    *   Configure environment for `plantuml` and `graphviz` (Included in `SPHINX_ENV_INSTALL`, Sphinx Environment via install.sh and install.bat)

This is your *.rst* file code example to create **PlantUML Diagram(s)**  `<http://plantuml.com/>`_:

.. tabularcolumns:: |p{\dimexpr 0.2\linewidth-2\tabcolsep}|
                     p{\dimexpr 0.6\linewidth-2\tabcolsep}|

.. list-table:: *PlantUML* Options
    :header-rows: 1
    :class: longtable

    * - **Option**
      - **Values**
    * - `:align:`
      - *left*, *center* or *right*
    * - `:scale:`
      - *0-100* percentage value
    * - `:caption:`
      - *text* to label Figure

*   Example 01

    .. code-block:: none

        .. uml::
            :scale: 75
            :align: center
            :caption: plantuml_example01

            Alice -> Bob: Hi!
            Alice <- Bob: How are you?

    Rendered

    .. uml::
        :scale: 75
        :align: center
        :caption: plantuml_example01

        Alice -> Bob: Hi!
        Alice <- Bob: How are you?

.. raw:: latex

    \newpage

*   Example 02

    .. code-block:: none

        .. uml::
            :scale: 75
            :align: center
            :caption: plantuml_example02

            Foo <|-- Bar

    Rendered

    .. uml::
        :scale: 75
        :align: center
        :caption: plantuml_example02

        Foo <|-- Bar

.. raw:: latex

    \newpage

*   Example 03

    .. note::

        Using `@startuml` and `@enduml` is not required but is proper formatting to move easily to a .uml file later.

    .. code-block:: none

        .. uml::
            :scale: 75
            :align: center
            :caption: plantuml_example03

            @startuml

            'style options
            skinparam monochrome true
            skinparam circledCharacterRadius 0
            skinparam circledCharacterFontSize 0
            skinparam classAttributeIconSize 0
            hide empty members

            Class01 <|-- Class02
            Class03 *-- Class04
            Class05 o-- Class06
            Class07 .. Class08
            Class09 -- Class10

            @enduml

    Rendered

    .. uml::
        :scale: 75
        :align: center
        :caption: plantuml_example03

        @startuml

        'style options
        skinparam monochrome true
        skinparam circledCharacterRadius 0
        skinparam circledCharacterFontSize 0
        skinparam classAttributeIconSize 0
        hide empty members

        Class01 <|-- Class02
        Class03 *-- Class04
        Class05 o-- Class06
        Class07 .. Class08
        Class09 -- Class10

        @enduml

.. raw:: latex

    \newpage

*   Example 04

    .. code-block:: none

        .. uml:: plantuml_example04.uml
            :scale: 75
            :align: center
            :caption: plantuml_example04

    Rendered (From loading .uml file)

    .. uml:: plantuml_example04.uml
        :scale: 75
        :align: center
        :caption: plantuml_example04

.. raw:: latex

    \newpage

*   Example 05

    .. literalinclude:: plantuml_example05.uml
        :caption: plantuml_example05.uml

    Rendered (From loading .uml file - same as Example04 just different file)

    .. uml:: plantuml_example05.uml
        :scale: 75
        :align: center
        :caption: plantuml_example05

.. raw:: latex

    \newpage

*   Example 06

    .. literalinclude:: plantuml_example06.uml
        :caption: plantuml_example06.uml

    Rendered (From loading .uml file - same as Example04 just different file)

    .. uml:: plantuml_example06.uml
        :scale: 55
        :align: center
        :caption: plantuml_example06

.. raw:: latex

    \newpage

*   Example 07

    .. literalinclude:: plantuml_example07.uml
        :caption: plantuml_example07.uml

    .. raw:: latex

        \newpage

    Rendered (From loading .uml file - same as Example04 just different file)

    .. uml:: plantuml_example07.uml
        :scale: 55
        :align: center
        :caption: plantuml_example07

.. raw:: latex

    \newpage

*   Example 08

    .. literalinclude:: plantuml_example08.uml
        :caption: plantuml_example08.uml

    .. raw:: latex

        \newpage

    Rendered (From loading .uml file - same as Example04 just different file)

    .. uml:: plantuml_example08.uml
        :scale: 45
        :align: center
        :caption: plantuml_example08

.. raw:: latex

    \newpage

*   Example 09

    .. literalinclude:: plantuml_example09.uml
        :caption: plantuml_example09.uml

    .. raw:: latex

        \newpage

    Rendered (From loading .uml file - same as Example04 just different file)

    .. uml:: plantuml_example09.uml
        :scale: 55
        :align: center
        :caption: plantuml_example09

.. raw:: latex

    \newpage

*   Example 10

    .. literalinclude:: plantuml_example10.uml
        :caption: plantuml_example10.uml

    .. raw:: latex

        \newpage

    Rendered (From loading .uml file - same as Example04 just different file)

    .. uml:: plantuml_example10.uml
        :scale: 65
        :align: center
        :caption: plantuml_example10

.. raw:: latex

    \newpage

*   Example 11

    .. literalinclude:: plantuml_example11.uml
        :caption: plantuml_example11.uml

    Rendered (From loading .uml file - same as Example04 just different file)

    .. uml:: plantuml_example11.uml
        :scale: 100
        :align: center
        :caption: plantuml_example11

.. raw:: latex

    \newpage

*   Example 12

    .. literalinclude:: plantuml_example12.uml
        :caption: plantuml_example12.uml

    Rendered (From loading .uml file - same as Example04 just different file)

    .. uml:: plantuml_example12.uml
        :scale: 100
        :align: center
        :caption: plantuml_example12

.. raw:: latex

    \newpage
