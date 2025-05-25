<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Planificador de Rutas y Entregas</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        /* Estilos generales del cuerpo y contenedor de la aplicación */
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f3f4f6; /* Fondo gris claro */
            display: flex;
            justify-content: center;
            align-items: flex-start; /* Alinea el contenido al inicio verticalmente */
            min-height: 100vh; /* Altura mínima de la ventana */
            padding: 20px; /* Espaciado alrededor */
        }
        #app-container {
            background-color: #ffffff; /* Fondo blanco para el contenedor principal */
            border-radius: 1rem; /* Bordes redondeados */
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); /* Sombra sutil */
            padding: 2rem; /* Relleno interno */
            width: 100%;
            max-width: 800px; /* Ancho máximo para el contenedor */
            margin-top: 20px; /* Margen superior */
        }
        /* Estilos para las secciones de los pasos */
        .step-section {
            display: none; /* Oculto por defecto */
        }
        .step-section.active {
            display: block; /* Visible cuando está activo */
        }
        /* Estilos para los botones primarios */
        .button-primary {
            @apply bg-blue-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-blue-700 transition duration-300 ease-in-out shadow-md;
        }
        /* Estilos para los botones secundarios */
        .button-secondary {
            @apply bg-gray-200 text-gray-800 px-6 py-3 rounded-lg font-semibold hover:bg-gray-300 transition duration-300 ease-in-out shadow-sm;
        }
        /* Oculta las flechas de los inputs tipo number en navegadores WebKit */
        input[type="number"]::-webkit-inner-spin-button,
        input[type="number"]::-webkit-outer-spin-button {
            -webkit-appearance: none;
            margin: 0;
        }
        /* Oculta las flechas de los inputs tipo number en Firefox */
        input[type="number"] {
            -moz-appearance: textfield;
        }
    </style>
</head>
<body class="bg-gray-100 p-4">
    <div id="app-container" class="max-w-3xl mx-auto bg-white p-8 rounded-xl shadow-xl">
        <h1 class="text-3xl font-bold text-center text-gray-800 mb-8">Planificador de Rutas y Entregas</h1>

        <div id="step1" class="step-section active">
            <h2 class="text-2xl font-semibold text-gray-700 mb-6">Paso 1: Disponibilidad de Camiones</h2>
            <div class="space-y-4">
                <div>
                    <label for="truckGrandeAvailable" class="block text-gray-700 text-lg font-medium mb-2">¿Está disponible el camión GRANDE?</label>
                    <select id="truckGrandeAvailable" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 text-lg">
                        <option value="yes">Sí</option>
                        <option value="no">No</option>
                    </select>
                </div>
                <div>
                    <label for="truckPequenoAvailable" class="block text-gray-700 text-lg font-medium mb-2">¿Está disponible el camión PEQUEÑO?</label>
                    <select id="truckPequenoAvailable" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 text-lg">
                        <option value="yes">Sí</option>
                        <option value="no">No</option>
                    </select>
                </div>
            </div>
            <div class="flex justify-end mt-8">
                <button id="nextStep1" class="button-primary">Siguiente</button>
            </div>
        </div>

        <div id="step2" class="step-section">
            <h2 class="text-2xl font-semibold text-gray-700 mb-6">Paso 2: Seleccionar Área de Distribución</h2>
            <div class="space-y-4">
                <div>
                    <label for="areaSelect" class="block text-gray-700 text-lg font-medium mb-2">Seleccione el área a visitar:</label>
                    <select id="areaSelect" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 text-lg">
                        </select>
                </div>
            </div>
            <div class="flex justify-between mt-8">
                <button id="prevStep2" class="button-secondary">Anterior</button>
                <button id="nextStep2" class="button-primary">Siguiente</button>
            </div>
        </div>

        <div id="step3" class="step-section">
            <h2 class="text-2xl font-semibold text-gray-700 mb-6">Paso 3: Seleccionar Ruta</h2>
            <div class="space-y-4">
                <div>
                    <label for="routeSelect" class="block text-gray-700 text-lg font-medium mb-2">Seleccione la ruta a tomar:</label>
                    <select id="routeSelect" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 text-lg">
                        </select>
                </div>
            </div>
            <div class="flex justify-between mt-8">
                <button id="prevStep3" class="button-secondary">Anterior</button>
                <button id="nextStep3" class="button-primary">Siguiente</button>
            </div>
        </div>

        <div id="step4" class="step-section">
            <h2 class="text-2xl font-semibold text-gray-700 mb-6">Paso 4: Tomar Pedidos de Clientes</h2>
            <div id="clientOrderContainer" class="space-y-6">
                </div>
            <div class="flex justify-between mt-8">
                <button id="prevStep4" class="button-secondary">Anterior</button> <button id="nextStep4" class="button-primary">Finalizar Pedidos</button>
            </div>
        </div>

        <div id="step5" class="step-section">
            <h2 class="text-2xl font-semibold text-gray-700 mb-6">Paso 5: Resumen de la Ruta y Asignación de Camión</h2>
            <div id="summaryContent" class="space-y-4 text-gray-700">
                </div>
            <div class="flex justify-between mt-8">
                <button id="prevStep5" class="button-secondary">Volver a Pedidos</button>
                <button id="restartApp" class="button-primary">Iniciar Nuevo Plan</button>
            </div>
        </div>

        <div id="messageBox" class="fixed inset-0 bg-gray-800 bg-opacity-75 flex items-center justify-center p-4 z-50 hidden">
            <div class="bg-white p-8 rounded-xl shadow-2xl max-w-sm w-full text-center">
                <h3 id="messageTitle" class="text-xl font-bold mb-4 text-gray-800"></h3>
                <p id="messageText" class="text-gray-700 mb-6"></p>
                <button id="closeMessageBox" class="button-primary">Aceptar</button>
            </div>
        </div>
    </div>

    <script>
        // --- Definiciones de Datos ---
        // Datos de los camiones: id, nombre, capacidad en kg y costo por ruta.
        const TRUCKS = [
            { id: 'grande', name: 'GRANDE', capacityKg: 10000, cost: 500 },
            { id: 'pequeno', name: 'PEQUEÑO', capacityKg: 3000, cost: 200 },
            { id: 'adicional', name: 'ADICIONAL', capacityKg: 8000, cost: 400 } // Detalles del camión adicional
        ];

        // Datos de los productos: id, nombre y peso por unidad en kg.
        const PRODUCTS = [
            { id: 'leche', name: 'Cajas de Leche', weightPerUnitKg: 10 },
            { id: 'azucar', name: 'Sacos de Azúcar', weightPerUnitKg: 25 },
            { id: 'harina', name: 'Bolsas de Harina', weightPerUnitKg: 5 },
            { id: 'aceite', name: 'Botellas de Aceite', weightPerUnitKg: 2 }
        ];

        // Estructura de datos para Áreas, Rutas y Clientes.
        // Cada área tiene rutas, y cada ruta tiene clientes con productos disponibles.
        const AREAS_ROUTES_CLIENTS = [
            {
                name: 'Área Norte',
                routes: [
                    {
                        name: 'Ruta N1',
                        baseCost: 150, // Costo base de esta ruta
                        clients: [
                            { name: 'Cliente N1A', products: ['leche', 'azucar'] },
                            { name: 'Cliente N1B', products: ['harina', 'aceite'] },
                            { name: 'Cliente N1C', products: ['leche', 'harina'] },
                            { name: 'Cliente N1D', products: ['azucar', 'aceite'] },
                            { name: 'Cliente N1E', products: ['leche'] }
                        ]
                    },
                    {
                        name: 'Ruta N2',
                        baseCost: 180,
                        clients: [
                            { name: 'Cliente N2A', products: ['azucar'] },
                            { name: 'Cliente N2B', products: ['leche', 'aceite'] },
                            { name: 'Cliente N2C', products: ['harina'] },
                            { name: 'Cliente N2D', products: ['leche', 'azucar', 'harina'] }
                        ]
                    }
                ]
            },
            {
                name: 'Área Sur',
                routes: [
                    {
                        name: 'Ruta S1',
                        baseCost: 200,
                        clients: [
                            { name: 'Cliente S1A', products: ['aceite', 'harina'] },
                            { name: 'Cliente S1B', products: ['leche', 'azucar'] },
                            { name: 'Cliente S1C', products: ['harina', 'aceite'] },
                            { name: 'Cliente S1D', products: ['azucar'] }
                        ]
                    },
                    {
                        name: 'Ruta S2',
                        baseCost: 220,
                        clients: [
                            { name: 'Cliente S2A', products: ['leche', 'azucar'] },
                            { name: 'Cliente S2B', products: ['harina'] },
                            { name: 'Cliente S2C', products: ['aceite'] },
                            { name: 'Cliente S2D', products: ['leche', 'harina'] },
                            { name: 'Cliente S2E', products: ['azucar', 'aceite'] }
                        ]
                    }
                ]
            }
        ];

        // --- Variables de Estado Globales ---
        let currentStep = 1; // Controla el paso actual de la aplicación
        let truckAvailability = { // Disponibilidad inicial de los camiones de la empresa
            grande: true,
            pequeno: true
        };
        let selectedArea = null; // Área seleccionada por el usuario
        let selectedRoute = null; // Ruta seleccionada por el usuario
        let clientOrders = []; // Almacena los pedidos de los clientes: [{ clientName: '...', orders: [{ productId: '...', units: N }] }]

        // --- Elementos del DOM ---
        const appContainer = document.getElementById('app-container');
        const stepSections = document.querySelectorAll('.step-section'); // Todas las secciones de pasos
        const messageBox = document.getElementById('messageBox'); // Caja de mensajes personalizada
        const messageTitle = document.getElementById('messageTitle'); // Título de la caja de mensajes
        const messageText = document.getElementById('messageText'); // Texto de la caja de mensajes
        const closeMessageBoxButton = document.getElementById('closeMessageBox'); // Botón para cerrar la caja de mensajes

        // --- Funciones de Ayuda ---

        /**
         * Muestra una caja de mensajes personalizada en lugar de alert().
         * @param {string} title - El título del mensaje.
         * @param {string} message - El contenido del mensaje.
         */
        function showMessageBox(title, message) {
            messageTitle.textContent = title;
            messageText.textContent = message;
            messageBox.classList.remove('hidden'); // Hace visible la caja de mensajes
        }

        /**
         * Oculta la caja de mensajes personalizada.
         */
        function hideMessageBox() {
            messageBox.classList.add('hidden'); // Oculta la caja de mensajes
        }

        /**
         * Navega a un paso específico de la aplicación.
         * @param {number} stepNum - El número del paso al que navegar.
         */
        function goToStep(stepNum) {
            stepSections.forEach(section => section.classList.remove('active')); // Oculta todas las secciones
            document.getElementById(`step${stepNum}`).classList.add('active'); // Muestra la sección del paso deseado
            currentStep = stepNum; // Actualiza el paso actual
        }

        /**
         * Calcula el peso total de todos los pedidos actuales.
         * @returns {number} El peso total en kilogramos.
         */
        function calculateTotalOrderWeight() {
            let totalWeight = 0;
            clientOrders.forEach(clientOrder => {
                clientOrder.orders.forEach(order => {
                    const product = PRODUCTS.find(p => p.id === order.productId);
                    if (product) {
                        totalWeight += product.weightPerUnitKg * order.units;
                    }
                });
            });
            return totalWeight;
        }

        /**
         * Renderiza el paso actual basándose en la variable global `currentStep`.
         * Llama a las funciones específicas de cada paso para poblar el contenido.
         */
        function renderStep() {
            goToStep(currentStep); // Cambia la visibilidad de las secciones
            switch (currentStep) {
                case 1:
                    // El Paso 1 ya está renderizado por defecto en el HTML
                    break;
                case 2:
                    populateAreas(); // Llena el selector de áreas
                    break;
                case 3:
                    populateRoutes(); // Llena el selector de rutas
                    break;
                case 4:
                    populateClientOrderForms(); // Genera los formularios de pedidos para cada cliente
                    break;
                case 5:
                    evaluateAndDisplaySummary(); // Evalúa y muestra el resumen final
                    break;
            }
        }

        // --- Lógica del Paso 1 ---
        document.getElementById('nextStep1').addEventListener('click', () => {
            // Actualiza la disponibilidad de los camiones según la selección del usuario
            truckAvailability.grande = document.getElementById('truckGrandeAvailable').value === 'yes';
            truckAvailability.pequeno = document.getElementById('truckPequenoAvailable').value === 'yes';
            goToStep(2); // Avanza al siguiente paso
            renderStep(); // Renderiza el nuevo paso
        });

        // --- Lógica del Paso 2 ---
        const areaSelect = document.getElementById('areaSelect');
        /**
         * Llena el selector de áreas con las opciones disponibles.
         */
        function populateAreas() {
            areaSelect.innerHTML = '<option value="">Seleccione un área</option>'; // Opción por defecto
            AREAS_ROUTES_CLIENTS.forEach(area => {
                const option = document.createElement('option');
                option.value = area.name;
                option.textContent = area.name;
                areaSelect.appendChild(option);
            });
            // Restaura la selección si ya se había elegido un área previamente
            areaSelect.value = selectedArea ? selectedArea.name : '';
        }

        document.getElementById('nextStep2').addEventListener('click', () => {
            const selectedAreaName = areaSelect.value;
            if (!selectedAreaName) {
                showMessageBox('Error', 'Por favor, seleccione un área.'); // Muestra un error si no se selecciona nada
                return;
            }
            selectedArea = AREAS_ROUTES_CLIENTS.find(area => area.name === selectedAreaName); // Guarda el área seleccionada
            goToStep(3); // Avanza al siguiente paso
            renderStep(); // Renderiza el nuevo paso
        });

        document.getElementById('prevStep2').addEventListener('click', () => {
            goToStep(1); // Regresa al paso anterior
            renderStep(); // Renderiza el nuevo paso
        });

        // --- Lógica del Paso 3 ---
        const routeSelect = document.getElementById('routeSelect');
        /**
         * Llena el selector de rutas con las opciones disponibles para el área seleccionada.
         */
        function populateRoutes() {
            routeSelect.innerHTML = '<option value="">Seleccione una ruta</option>'; // Opción por defecto
            if (selectedArea) {
                selectedArea.routes.forEach(route => {
                    const option = document.createElement('option');
                    option.value = route.name;
                    option.textContent = route.name;
                    routeSelect.appendChild(option);
                });
            }
            // Restaura la selección si ya se había elegido una ruta previamente
            routeSelect.value = selectedRoute ? selectedRoute.name : '';
        }

        document.getElementById('nextStep3').addEventListener('click', () => {
            const selectedRouteName = routeSelect.value;
            if (!selectedRouteName) {
                showMessageBox('Error', 'Por favor, seleccione una ruta.'); // Muestra un error si no se selecciona nada
                return;
            }
            selectedRoute = selectedArea.routes.find(route => route.name === selectedRouteName); // Guarda la ruta seleccionada
            clientOrders = []; // Reinicia los pedidos al seleccionar una nueva ruta
            goToStep(4); // Avanza al siguiente paso
            renderStep(); // Renderiza el nuevo paso
        });

        document.getElementById('prevStep3').addEventListener('click', () => {
            selectedArea = null; // Limpia la selección de área al regresar
            goToStep(2); // Regresa al paso anterior
            renderStep(); // Renderiza el nuevo paso
        });

        // --- Lógica del Paso 4 ---
        const clientOrderContainer = document.getElementById('clientOrderContainer');

        /**
         * Genera dinámicamente los formularios de toma de pedidos para cada cliente en la ruta seleccionada.
         */
        function populateClientOrderForms() {
            clientOrderContainer.innerHTML = ''; // Limpia formularios anteriores
            if (!selectedRoute || !selectedRoute.clients) {
                showMessageBox('Error', 'No hay clientes para esta ruta.');
                return;
            }

            selectedRoute.clients.forEach((client, clientIndex) => {
                const clientDiv = document.createElement('div');
                clientDiv.className = 'bg-gray-50 p-6 rounded-lg shadow-sm border border-gray-200';
                clientDiv.innerHTML = `
                    <h3 class="text-xl font-semibold text-gray-800 mb-4">${client.name}</h3>
                    <div class="mb-4">
                        <label class="inline-flex items-center text-gray-700 text-lg font-medium">
                            <input type="checkbox" class="form-checkbox h-5 w-5 text-blue-600 rounded" id="client${clientIndex}Requested">
                            <span class="ml-2">¿Solicitó producto?</span>
                        </label>
                    </div>
                    <div id="client${clientIndex}Products" class="space-y-3 hidden">
                        </div>
                `;
                clientOrderContainer.appendChild(clientDiv);

                const requestedCheckbox = document.getElementById(`client${clientIndex}Requested`);
                const productsDiv = document.getElementById(`client${clientIndex}Products`);

                // Muestra u oculta los inputs de productos según si el cliente solicitó o no
                requestedCheckbox.addEventListener('change', () => {
                    productsDiv.classList.toggle('hidden', !requestedCheckbox.checked);
                });

                // Llena los productos disponibles para cada cliente
                client.products.forEach(productId => {
                    const product = PRODUCTS.find(p => p.id === productId);
                    if (product) {
                        const productInputDiv = document.createElement('div');
                        productInputDiv.className = 'flex items-center space-x-3';
                        productInputDiv.innerHTML = `
                            <label for="client${clientIndex}Product${product.id}" class="text-gray-700 text-base">${product.name} (Peso: ${product.weightPerUnitKg} kg/unidad):</label>
                            <input type="number" id="client${clientIndex}Product${product.id}"
                                class="w-24 p-2 border border-gray-300 rounded-md text-center text-lg"
                                min="0" value="0">
                        `;
                        productsDiv.appendChild(productInputDiv);
                    }
                });

                // Restaura los pedidos anteriores si existen (útil al regresar a este paso)
                const existingOrder = clientOrders.find(o => o.clientName === client.name);
                if (existingOrder) {
                    requestedCheckbox.checked = true;
                    productsDiv.classList.remove('hidden');
                    existingOrder.orders.forEach(order => {
                        const input = document.getElementById(`client${clientIndex}Product${order.productId}`);
                        if (input) input.value = order.units;
                    });
                }
            });
        }

        document.getElementById('nextStep4').addEventListener('click', () => {
            clientOrders = []; // Limpia los pedidos anteriores antes de recolectar los nuevos
            let hasOrders = false; // Bandera para verificar si se tomó algún pedido

            selectedRoute.clients.forEach((client, clientIndex) => {
                const requestedCheckbox = document.getElementById(`client${clientIndex}Requested`);
                const clientCurrentOrders = { clientName: client.name, orders: [] };

                if (requestedCheckbox.checked) {
                    client.products.forEach(productId => {
                        const input = document.getElementById(`client${clientIndex}Product${productId}`);
                        const units = parseInt(input.value);
                        if (!isNaN(units) && units > 0) {
                            clientCurrentOrders.orders.push({ productId: productId, units: units });
                            hasOrders = true;
                        }
                    });
                }
                clientOrders.push(clientCurrentOrders);
            });

            // Si no se tomaron pedidos, muestra una advertencia y permite continuar
            if (!hasOrders) {
                showMessageBox('Advertencia', 'No se han tomado pedidos para ningún cliente en esta ruta. ¿Desea continuar?');
                // Al cerrar la advertencia, avanza al siguiente paso
                messageBox.querySelector('#closeMessageBox').onclick = () => {
                    hideMessageBox();
                    goToStep(5);
                    renderStep();
                };
            } else {
                goToStep(5); // Avanza al siguiente paso
                renderStep(); // Renderiza el nuevo paso
            }
        });

        document.getElementById('prevStep4').addEventListener('click', () => {
            goToStep(3); // Regresa al paso anterior
            renderStep(); // Renderiza el nuevo paso
        });

        // --- Lógica del Paso 5 (Resumen y Asignación de Camión) ---
        const summaryContent = document.getElementById('summaryContent');

        /**
         * Evalúa las opciones de camiones, asigna el más adecuado y muestra el resumen final.
         */
        function evaluateAndDisplaySummary() {
            summaryContent.innerHTML = ''; // Limpia el resumen anterior

            const totalWeight = calculateTotalOrderWeight(); // Calcula el peso total de todos los pedidos
            let assignedTruck = null; // Camión asignado
            let minCost = Infinity; // Costo mínimo encontrado

            // Filtra los camiones disponibles y que pueden llevar el peso total
            let possibleTrucks = [];

            // Primero, considera solo los camiones de la empresa si están disponibles y tienen capacidad
            ['grande', 'pequeno'].forEach(truckId => {
                const truck = TRUCKS.find(t => t.id === truckId);
                if (truck && truckAvailability[truckId] && totalWeight <= truck.capacityKg) {
                    possibleTrucks.push(truck);
                }
            });

            // Si no hay camiones de la empresa que puedan manejar el peso o estén disponibles, considera el 'adicional'
            // El camión adicional siempre está "disponible" en el sentido de que se puede contratar.
            const adicionalTruck = TRUCKS.find(t => t.id === 'adicional');
            if (adicionalTruck && totalWeight <= adicionalTruck.capacityKg) {
                possibleTrucks.push(adicionalTruck);
            }

            // Si el peso total es mayor que 0 pero ningún camión puede manejarlo
            if (totalWeight > 0 && possibleTrucks.length === 0) {
                summaryContent.innerHTML = `
                    <p class="text-red-600 font-bold text-xl mb-4">¡Atención! El peso total de los pedidos (${totalWeight.toFixed(2)} kg) excede la capacidad de todos los camiones disponibles.</p>
                    <p class="text-red-600">No se puede asignar un camión para esta ruta. Considere reducir el volumen de pedidos o buscar un camión de mayor capacidad.</p>
                `;
                return;
            } else if (totalWeight === 0) {
                 // Si no hay pedidos, no se necesita asignar un camión
                 summaryContent.innerHTML = `
                    <p class="text-blue-600 font-bold text-xl mb-4">No se realizaron pedidos en esta ruta.</p>
                    <p>No se necesita asignar un camión para esta ruta.</p>
                `;
                return;
            }


            // Encuentra el camión más barato entre los que pueden manejar el peso
            possibleTrucks.forEach(truck => {
                if (truck.cost < minCost) {
                    minCost = truck.cost;
                    assignedTruck = truck;
                }
            });

            // Calcula el costo total de transporte, incluyendo el costo base de la ruta
            let totalTransportCost = 0;
            if (assignedTruck && selectedRoute) {
                totalTransportCost = assignedTruck.cost + selectedRoute.baseCost;
            }

            // --- Construcción del HTML del resumen ---
            let summaryHtml = `<div class="mb-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
                                    <h3 class="text-xl font-bold text-blue-800 mb-2">Resumen General de la Ruta</h3>
                                    <p><span class="font-semibold">Área:</span> ${selectedArea.name}</p>
                                    <p><span class="font-semibold">Ruta:</span> ${selectedRoute.name}</p>
                                    <p><span class="font-semibold">Peso Total de Pedidos:</span> ${totalWeight.toFixed(2)} kg</p>
                                </div>`;

            if (assignedTruck) {
                // Si se asignó un camión, muestra sus detalles
                summaryHtml += `
                    <div class="mb-6 p-4 bg-green-50 rounded-lg border border-green-200">
                        <h3 class="text-xl font-bold text-green-800 mb-2">Asignación de Camión</h3>
                        <p><span class="font-semibold">Camión Asignado:</span> ${assignedTruck.name}</p>
                        <p><span class="font-semibold">Capacidad del Camión:</span> ${assignedTruck.capacityKg} kg</p>
                        <p><span class="font-semibold">Costo del Camión:</span> $${assignedTruck.cost.toFixed(2)}</p>
                        <p><span class="font-semibold">Costo Base de la Ruta:</span> $${selectedRoute.baseCost.toFixed(2)}</p>
                        <p><span class="font-semibold text-xl">Costo Total de Transporte:</span> <span class="text-xl font-bold text-green-700">$${totalTransportCost.toFixed(2)}</span></p>
                        <p class="text-sm text-gray-600 mt-2">Nota: El costo total incluye el costo del camión y el costo base de la ruta.</p>
                    </div>
                `;
            } else {
                 // Si no se pudo asignar un camión (aunque ya se manejó el caso de peso excesivo arriba)
                 summaryHtml += `
                    <div class="mb-6 p-4 bg-red-50 rounded-lg border border-red-200">
                        <h3 class="text-xl font-bold text-red-800 mb-2">Asignación de Camión</h3>
                        <p>No se pudo asignar un camión que cumpla con la capacidad o disponibilidad para el peso total de los pedidos.</p>
                    </div>
                `;
            }

            // Sección de detalle de pedidos por cliente
            summaryHtml += `
                <div class="mb-6 p-4 bg-purple-50 rounded-lg border border-purple-200">
                    <h3 class="text-xl font-bold text-purple-800 mb-2">Detalle de Pedidos por Cliente</h3>
                    <ul class="list-disc pl-5 space-y-2">
            `;

            let hasAnyOrder = false; // Bandera para saber si hay algún pedido en general
            clientOrders.forEach(clientOrder => {
                if (clientOrder.orders.length > 0) {
                    hasAnyOrder = true;
                    summaryHtml += `<li><span class="font-semibold">${clientOrder.clientName}:</span>`;
                    summaryHtml += `<ul class="list-circle pl-5 mt-1 space-y-1">`;
                    clientOrder.orders.forEach(order => {
                        const product = PRODUCTS.find(p => p.id === order.productId);
                        if (product) {
                            summaryHtml += `<li>${order.units} unidades de ${product.name} (${(order.units * product.weightPerUnitKg).toFixed(2)} kg)</li>`;
                        }
                    });
                    summaryHtml += `</ul></li>`;
                } else {
                    summaryHtml += `<li><span class="font-semibold">${clientOrder.clientName}:</span> No solicitó producto.</li>`;
                }
            });

            if (!hasAnyOrder) {
                summaryHtml += `<li>No se registraron pedidos para ningún cliente en esta ruta.</li>`;
            }
            summaryHtml += `</ul></div>`;

            // Sección de orden de entrega sugerido
            summaryHtml += `
                <div class="p-4 bg-yellow-50 rounded-lg border border-yellow-200">
                    <h3 class="text-xl font-bold text-yellow-800 mb-2">Orden de Entrega Sugerido</h3>
                    <p class="text-gray-700">El orden de entrega sugerido es el orden en que los clientes aparecen en la ruta:</p>
                    <ol class="list-decimal pl-5 mt-2 space-y-1">
            `;
            selectedRoute.clients.forEach(client => {
                summaryHtml += `<li>${client.name}</li>`;
            });
            summaryHtml += `
                    </ol>
                    <p class="text-sm text-gray-600 mt-2">
                        Nota: Para una optimización más avanzada del orden de entrega (ej. minimizando distancia), se requeriría un algoritmo de optimización de rutas (como el Problema del Viajante) y datos geográficos, lo cual está fuera del alcance de esta aplicación básica.
                    </p>
                </div>
            `;

            summaryContent.innerHTML = summaryHtml; // Inserta el HTML generado en el contenedor de resumen
        }

        document.getElementById('prevStep5').addEventListener('click', () => {
            goToStep(4); // Regresa al paso anterior
            renderStep(); // Renderiza el nuevo paso
        });

        document.getElementById('restartApp').addEventListener('click', () => {
            // Reinicia todas las variables de estado a sus valores iniciales
            currentStep = 1;
            truckAvailability = {
                grande: true,
                pequeno: true
            };
            selectedArea = null;
            selectedRoute = null;
            clientOrders = [];

            // Reinicia los elementos de la interfaz de usuario
            document.getElementById('truckGrandeAvailable').value = 'yes';
            document.getElementById('truckPequenoAvailable').value = 'yes';
            areaSelect.innerHTML = '';
            routeSelect.innerHTML = '';
            clientOrderContainer.innerHTML = '';
            summaryContent.innerHTML = '';

            renderStep(); // Vuelve al primer paso para iniciar un nuevo plan
        });

        // --- Listener para el botón de cerrar la caja de mensajes ---
        closeMessageBoxButton.addEventListener('click', hideMessageBox);

        // --- Renderizado Inicial al cargar la página ---
        renderStep();
    </script>
</body>
</html>